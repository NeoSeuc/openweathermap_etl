import json
import os

import pandas as pd
from sqlalchemy import create_engine, text


def get_avg_temperature(engine) -> pd.DataFrame:
    query = text("SELECT AVG(temp_c) FROM weather;")
    with engine.connect() as conn:
        result = conn.execute(query).scalar()
    return result


def get_unique_cities(engine) -> int:
    query = text("SELECT COUNT(DISTINCT city) FROM weather;")
    with engine.connect() as conn:
        result = conn.execute(query).scalar()
    return result


def get_avg_humidity_by_country(engine) -> list[dict]:
    query = text("""
        SELECT country, AVG(humidity) AS avg_humidity
        FROM weather
        GROUP BY country;
    """)
    with engine.connect() as conn:
        rows = conn.execute(query).mappings().all()
    return [dict(row) for row in rows]


def run_queries(db_path="local.db"):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.dirname(BASE_DIR)

    db_path = os.path.join(PROJECT_DIR, "local.db")
    engine = create_engine(f"sqlite:///{db_path}")

    results = {
        "avg_temp": get_avg_temperature(engine),
        "unique_cities": get_unique_cities(engine),
        "avg_humidity_by_country": get_avg_humidity_by_country(engine),
    }
    report_path = os.path.join(PROJECT_DIR, "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("[INFO] Report saved to report.json")
    return results
