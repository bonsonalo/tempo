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
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            return df
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path)
            return df
        elif file_path.endswith("xlsx") or file_path.endswith("xls"):
            df = pd.read_excel(file_path)
            return df
        else:
            logging.error("Only .csv, .xls, .xlsx, .json files are possible")
    else:
        raise FileNotFoundError(f"the {file_path} is not found")
        logging.error(f"The file {file_path} doesn't exist")




""" Missing value report """


def missing_values_report(df):

    missing = df.isna().sum()
    pct_missing = round(missing / len(df) * 100, 2)


    report = pd.DataFrame(
        {
            "n_missing": missing,
            "pct_missing": pct_missing
        }
    )

    report = report[report["n_missing"] > 0]      ## keep only columns with missing
    return report.sort_values(by="pct_missing", ascending=False)




def check_duplicates(df):

    duplicate_mask = df.duplicated(keep= False)   # this returns a bool. and keep = False means that list all duplicates as duplicates

    duplicates = df[duplicate_mask]
    n_duplicates = len(duplicates)

    logging.info(f"Found {n_duplicates} duplicate rows")

    return duplicates, n_duplicates