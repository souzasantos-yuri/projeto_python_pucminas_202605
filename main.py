from src.extract_data import extract_data
from src.transform_data import data_transformation
from src.load_data import load_data
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pipeline():
    try:
        logging.info(f"First stage: Extracting")
        df = extract_data()
        logging.info(f"Rows extracted: {len(df)}\n")

        logging.info(f"Second stage: Transforming")
        null_count = df.isna().sum().sum()
        logging.info(f"Null count before: {null_count}")
        df = data_transformation(df)
        null_count = df.isna().sum().sum()
        logging.info(f"Null count after: {null_count}\n")

        logging.info(f"Last stage: Loading")
        load_data(df)
        logging.info(f"Saved rows: {len(df)}\n")

        logging.info(f"Pipeline fully completed!")

    except Exception as e:
        logging.error(f"Error: {e}")
        import traceback
        traceback.print_exc()

pipeline()