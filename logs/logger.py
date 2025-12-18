import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))

import logging
import sys
from utils.config import LOGS_PATH

path = LOGS_PATH / "system.log"

logging.basicConfig(
    filename=path,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error("Exceção não tratada", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception