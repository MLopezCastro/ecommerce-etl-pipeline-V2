from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "raw" / "orders.csv"
OUTPUT_PATH = BASE_DIR / "data" / "output" / "orders_clean.csv"
LOG_PATH = BASE_DIR / "logs" / "etl.log"