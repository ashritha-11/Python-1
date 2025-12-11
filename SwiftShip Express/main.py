import logging
from extract import extract_all
from transform import transform
from load import load_data

# Logging for orchestrator
logger = logging.getLogger("etl")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("logs/etl.log")
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

def run_etl():
    logger.info("===== ETL Pipeline Started =====")
    try:
        # Extract
        logger.info("Step 1: Extracting data...")
        extract_all()
        logger.info("Step 1: Extract finished.")

        # Transform
        logger.info("Step 2: Transforming data...")
        transform()
        logger.info("Step 2: Transform finished.")

        # Load
        logger.info("Step 3: Loading data into Supabase...")
        load_data()
        logger.info("Step 3: Load finished.")

        logger.info("===== ETL Pipeline Completed Successfully =====")
    except Exception as e:
        logger.exception("ETL Pipeline failed: %s", e)

if __name__ == "__main__":
    run_etl()
