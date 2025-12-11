import os
import logging
import json
from pathlib import Path
import pandas as pd
from datetime import datetime

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")
LOG_DIR = Path("logs")

CLEAN_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("transform")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(LOG_DIR / "transform.log")
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

def latest_file(prefix: str) -> Path:
    files = list(RAW_DIR.glob(f"{prefix}_*.json"))
    if not files:
        logger.error("No valid raw file found for prefix %s", prefix)
        return None
    return max(files, key=lambda f: f.stat().st_mtime)

def transform():
    logger.info("Starting Transform stage...")

    live_file = latest_file("live_deliveries")
    route_file = latest_file("route_traffic")
    if not live_file or not route_file:
        logger.error("Missing raw files. Transform aborted.")
        return

    with open(live_file, "r", encoding="utf-8") as f:
        live = json.load(f)
    with open(route_file, "r", encoding="utf-8") as f:
        routes = json.load(f)

    # Check for failed extraction
    if isinstance(live, dict) and "error" in live:
        logger.error("Live delivery raw data indicates failure. Transform aborted.")
        return
    if isinstance(routes, dict) and "error" in routes:
        logger.error("Route traffic raw data indicates failure. Transform aborted.")
        return

    live_df = pd.DataFrame(live)
    route_df = pd.DataFrame(routes)

    # Merge on source city
    merged_df = live_df.merge(route_df, left_on="source_city", right_on="city", how="left")

    # Compute delay in minutes
    merged_df["dispatch_time"] = pd.to_datetime(merged_df["dispatch_time"])
    merged_df["expected_delivery_time"] = pd.to_datetime(merged_df["expected_delivery_time"])
    merged_df["actual_delivery_time"] = pd.to_datetime(merged_df["actual_delivery_time"])
    merged_df["delay_minutes"] = (merged_df["actual_delivery_time"] - merged_df["expected_delivery_time"]).dt.total_seconds() / 60.0
    merged_df["is_delayed"] = merged_df["delay_minutes"] > 0

    clean_file = CLEAN_DIR / f"clean_data_{datetime.now().strftime('%Y%m%dT%H%M%S')}.csv"
    merged_df.to_csv(clean_file, index=False)
    logger.info("Transform finished. Clean data saved: %s", clean_file)

if __name__ == "__main__":
    transform()
