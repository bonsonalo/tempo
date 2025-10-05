import logging
import sys
from pathlib import Path

def setup_logging():
     
    Path("logs").mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format= "%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler('logs/processing.py'),
            logging.StreamHandler()
        ]
    )
    