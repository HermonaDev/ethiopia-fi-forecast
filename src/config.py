import os

# Paths
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(ROOT_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(ROOT_DIR, "data", "processed")
FIGURES_DIR = os.path.join(ROOT_DIR, "reports", "figures")

# Constants
TARGET_COLUMN = "ACC_OWNERSHIP"
GOAL_VALUE = 60.0
BASE_YEAR = 2024
