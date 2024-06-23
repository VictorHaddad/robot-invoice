from dotenv import dotenv_values
from typing import Dict, List
from datetime import datetime
import logging
import os

logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

config = dotenv_values()
logger = logging.getLogger()
today = datetime.now().strftime("%d-%m-%Y")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FULL_SPREADSHEETS = r'C:\Users\vhadd\OneDrive\Desktop\robot-notas-fiscais\spreadsheets'

MONGO_HOST = config.get("HOST_MONGO")
MONGO_DATABASE = config.get("DATABASE_MONGO")