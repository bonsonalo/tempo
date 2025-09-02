import os
import pandas as pd
import numpy as np
import logging

# Get project root (one level above src/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Logs folder inside project root
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "file_utils.log"),
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)



def load_data(file_path):
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        logging.error(f"The file {file_path} doesn't exist")
        return None
