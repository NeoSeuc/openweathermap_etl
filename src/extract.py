from datetime import datetime
from dotenv import load_dotenv
from src.openweathermap_api import OpenWeatherMapAPI
import os

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
if OPENWEATHER_API_KEY is None:
    raise ValueError("OPENWEATHER_API_KEY not found in environment variables.")

openweathermap_api = OpenWeatherMapAPI(api_key=OPENWEATHER_API_KEY)


def extract_weather_data(lat: float, lon: float):
    response = openweathermap_api.get_current_weather_data(lat, lon)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.dirname(BASE_DIR)

    today = datetime.today().strftime("%Y-%m-%d")
    raw_dir = os.path.join(PROJECT_DIR, "data", "raw", today)
    os.makedirs(raw_dir, exist_ok=True)

    raw_path = os.path.join(raw_dir, "response.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        import json
        json.dump(response, f, indent=2, ensure_ascii=False)

    return response, raw_path
