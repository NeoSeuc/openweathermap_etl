import pandas as pd
import numpy as np


def transform_weather_data(raw_data: dict) -> pd.DataFrame:
    """
    Transform raw weather API response into a clean DataFrame.

    Args:
        raw_data (dict): JSON response from OpenWeatherMap API.

    Returns:
        pd.DataFrame: Cleaned and transformed data.
    """
    # дістаємо значення з raw_data
    city = raw_data.get("name")
    country = raw_data.get("sys", {}).get("country")
    temp_k = raw_data.get("main", {}).get("temp")
    humidity = raw_data.get("main", {}).get("humidity")
    wind_speed = raw_data.get("wind", {}).get("speed")
    description = raw_data.get("weather", [{}])[0].get("description")

    # конвертація температури
    temp_c = temp_k - 273.15 if temp_k is not None else np.nan

    # формуємо словник з потрібними полями
    clean_record = {
        "city": city,
        "country": country,
        "temp_k": temp_k,
        "temp_c": round(temp_c, 2) if temp_k is not None else np.nan,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "weather_description": description,
    }

    # створюємо DataFrame
    df = pd.DataFrame([clean_record])

    # замінюємо пусті значення на NaN
    df = df.replace({None: np.nan, "": np.nan})

    return df