import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Successfully read {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None
