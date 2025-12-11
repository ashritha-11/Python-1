"""
extract.py
Fetch Live Delivery API + Route Traffic API, save raw responses to data/raw/
with timestamped filenames, retry logic (max 3), and logging of failures.

Supports MOCK mode if APIs do not exist.
"""

import os
import json
import time
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, Any

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================
# CONFIG
# ============================
LIVE_API_URL = os.getenv("LIVE_DELIVERY_API_URL", "https://api.swiftshipexpress.in/v1/deliveries/live")
ROUTE_API_URL = os.getenv("ROUTE_TRAFFIC_API_URL", "https://api.swiftshipexpress.in/v1/traffic/routes")
API_KEY = os.getenv("SWIFTSHIP_API_KEY")

USE_MOCK_DATA = os.getenv("USE_MOCK_DATA", "False") == "True"

DATA_RAW_DIR = Path("data/raw")
DATA_MOCK_DIR = Path("data/mock")
LOG_DIR = Path("logs")

MAX_RETRIES = int(os.getenv("EXTRACT_MAX_RETRIES", "3"))
INITIAL_BACKOFF = float(os.getenv("EXTRACT_BACKOFF_SECONDS", "1.0"))
REQUEST_TIMEOUT = float(os.getenv("EXTRACT_TIMEOUT_SECONDS", "10.0"))

DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)
DATA_MOCK_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# ============================
# LOGGING
# ============================
logger = logging.getLogger("extract")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(LOG_DIR / "extract.log")
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(fmt)
ch.setFormatter(fmt)
logger.addHandler(fh)
logger.addHandler(ch)


# ============================
# HELPERS
# ============================
def utc_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def save_raw_response(name: str, data: Any) -> Path:
    filename = f"{name}_{utc_ts()}.json"
    path = DATA_RAW_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info("Saved raw response → %s", path)
    return path


def load_mock_data(name: str):
    mock_path = DATA_MOCK_DIR / f"{name}.json"
    if not mock_path.exists():
        logger.error("Mock file missing: %s", mock_path)
        return None

    logger.info("[%s] Using MOCK data → %s", name, mock_path)
    with open(mock_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    save_raw_response(name, data)
    return data


# ============================
# FETCH FUNCTION
# ============================
def fetch_with_retries(
    session: requests.Session,
    name: str,
    url: str,
    params=None,
    headers=None,
    max_retries=MAX_RETRIES,
    initial_backoff=INITIAL_BACKOFF,
    timeout=REQUEST_TIMEOUT,
):
    # Mock Mode
    if USE_MOCK_DATA:
        return load_mock_data(name)

    if headers is None:
        headers = {}

    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"

    attempt = 0
    backoff = initial_backoff

    while attempt < max_retries:
        attempt += 1
        try:
            logger.info("[%s] Attempt %d → GET %s", name, attempt, url)
            resp = session.get(url, params=params, headers=headers, timeout=timeout)
            resp.raise_for_status()

            try:
                data = resp.json()
            except ValueError:
                data = resp.text

            save_raw_response(name, data)
            return data

        except requests.RequestException as e:
            logger.error("[%s] Attempt %d FAILED: %s", name, attempt, e)

            if attempt >= max_retries:
                logger.error("[%s] All retries FAILED. Saving failure log.", name)
                save_raw_response(f"{name}_FAILURE", {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "url": url,
                    "error": str(e),
                })
                return None

            time.sleep(backoff)
            backoff *= 2


# ============================
# EXTRACT ORCHESTRATOR
# ============================
def extract_all():
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=1)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    results = {}

    results["live_deliveries"] = fetch_with_retries(session, "live_deliveries", LIVE_API_URL)
    results["route_traffic"] = fetch_with_retries(session, "route_traffic", ROUTE_API_URL)

    return results


# ============================
# MAIN
# ============================
if __name__ == "__main__":
    logger.info("🚀 Starting EXTRACT stage for SwiftShip Express...")
    data = extract_all()
    logger.info("✅ Extract stage completed. Keys fetched → %s", list(data.keys()))
