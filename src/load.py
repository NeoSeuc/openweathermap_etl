import os
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine


def load_weather_data(processed_data: pd.DataFrame):
    """
    Save processed weather data into Parquet and SQLite DB.

    Args:
        processed_data (pd.DataFrame): Cleaned weather data.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # шлях до src
    PROJECT_DIR = os.path.dirname(BASE_DIR)  # шлях до project

    today = datetime.today().strftime("%Y-%m-%d")
    processed_dir = os.path.join(PROJECT_DIR, "data", "processed", today)
    os.makedirs(processed_dir, exist_ok=True)

    parquet_path = os.path.join(processed_dir, "data.parquet")
    processed_data.to_parquet(parquet_path, index=False)

    print(f"[INFO] Processed data saved to {parquet_path}")

    db_path = os.path.join(PROJECT_DIR, "local.db")
    engine = create_engine(f"sqlite:///{db_path}")

    processed_data.to_sql("weather", engine, if_exists="append", index=False)

    print(f"[INFO] Processed data loaded into SQLite DB at {db_path}")

    return parquet_path, db_path
