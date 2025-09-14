# Openweathermap ETL

Simple ETL pipeline to extract weather data from `Openweathermap API`, transform it, and load it into a SQLite database.

## How to Use

1. Copy the `.env.example` file to `.env` and fill in your Openweathermap API key. from https://openweathermap.org/
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the ETL script:
   ```
   python etl.py
   ```
   
## How It Works

- **Extract**: Fetches weather data from Openweathermap API for a specified coordinates. Saves the raw JSON response to a file into the `/data/raw/yyyy-mm-dd/response.json` directory.

response.json example:  
```json
          {
        "coord": {
          "lon": 30.5233,
          "lat": 50.45
        },
        "weather": [
          {
            "id": 804,
            "main": "Clouds",
            "description": "overcast clouds",
            "icon": "04n"
          }
        ],
        "base": "stations",
        "main": {
          "temp": 288.34,
          "feels_like": 287.79,
          "temp_min": 288.34,
          "temp_max": 288.34,
          "pressure": 1027,
          "humidity": 72,
          "sea_level": 1027,
          "grnd_level": 1011
        },
        "visibility": 10000,
        "wind": {
          "speed": 2.38,
          "deg": 125,
          "gust": 5.79
        },
        "clouds": {
          "all": 100
        },
        "dt": 1757733439,
        "sys": {
          "type": 2,
          "id": 2003742,
          "country": "UA",
          "sunrise": 1757734229,
          "sunset": 1757780250
        },
        "timezone": 10800,
        "id": 696050,
        "name": "Pushcha-Vodytsya",
        "cod": 200
      }
```
- **Transform**: Cleans and formats the data into a structured format.
  - Converts temperature from Kelvin to Celsius.
  - Tales only relevant fields: `city`, `country`, `date`, `temperature`, , `wind_speed`, `humidity`, `weather_description`.
- **Load**: Save processed data to `/data/processed/yyyy-mm-dd/data.parquet`. Inserts the transformed data into a SQLite database.
- **Analytics**: Generate simple analytics and save the results as a `report.json` file
report.json example:
```json
{
  "avg_temp": 13.105,
  "unique_cities": 2,
  "avg_humidity_by_country": [
    {
      "country": "UA",
      "avg_humidity": 72.0
    }
  ]
}
```
