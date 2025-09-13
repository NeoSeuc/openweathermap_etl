import requests


class OpenWeatherMapAPI:
    def __init__(self, api_key: str):
        self.API_KEY = api_key

    def get_current_weather_data(self, lat: float, lon: float):
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.API_KEY}"

        if lat > 90 or lat < -90:
            raise ValueError("Latitude must be between -90 and 90.")

        if lon > 180 or lon < -180:
            raise ValueError("Longitude must be between -180 and 180.")

        return requests.get(api_url).json()
