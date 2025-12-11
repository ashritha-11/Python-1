import os
import logging
import time
import pandas as pd
from pathlib import Path
from supabase import create_client, Client
from dotenv import load_dotenv

# Load .env
env_path = os.path.join(os.getcwd(), ".env")
load_dotenv(env_path)

CLEAN_DIR = Path("data/clean")
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("load")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(LOG_DIR / "load.log")
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

# Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Supabase credentials not found in .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def load_latest_clean():
    files = list(CLEAN_DIR.glob("clean_data_*.csv"))
    if not files:
        logger.error("No clean CSV found.")
        return None
    latest = max(files, key=lambda f: f.stat().st_mtime)
    logger.info("Loaded clean dataset: %s", latest)
    return latest

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS public.delivery_analytics (
    id BIGSERIAL PRIMARY KEY,
    shipment_id TEXT,
    source_city TEXT,
    destination_city TEXT,
    dispatch_time TIMESTAMP,
    expected_delivery_time TIMESTAMP,
    actual_delivery_time TIMESTAMP,
    package_weight FLOAT,
    delivery_agent_id TEXT,
    delay_minutes FLOAT,
    is_delayed BOOLEAN,
    city TEXT,
    traffic_congestion_score FLOAT,
    average_speed FLOAT,
    weather_warnings TEXT
);
"""

def create_table_if_needed():
    try:
        supabase.postgrest.rpc("execute_sql", {"query": CREATE_TABLE_SQL}).execute()
        logger.info("Table created or already exists.")
    except Exception as e:
        logger.warning("Could not auto-create table. Run SQL manually. Error: %s", e)

def load_data():
    logger.info("Starting Load stage...")

    clean_file = load_latest_clean()
    if clean_file is None:
        return

    df = pd.read_csv(clean_file)
    create_table_if_needed()

    batch_size = 100
    for start in range(0, len(df), batch_size):
        batch = df.iloc[start:start+batch_size].to_dict(orient="records")
        try:
            supabase.table("delivery_analytics").insert(batch).execute()
            logger.info("Inserted %d rows", len(batch))
        except Exception as e:
            logger.error("Batch insert failed: %s", e)
            time.sleep(3)

    logger.info("Load complete.")

if __name__ == "__main__":
    load_data()
