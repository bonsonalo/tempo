import logging
import sys
from pathlib import Path

def setup_logging(log_level= logging.INFO):
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)


    log_format= "%(asctime)s - %(levelname)s - %(message)s"