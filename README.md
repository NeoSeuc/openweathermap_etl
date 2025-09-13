# Openweathermap ETL

Simple ETL pipeline to extract weather data from Openweathermap API, transform it, and load it into a SQLite database.

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
- **Transform**: Cleans and formats the data into a structured format.
- **Load**: Save processed data to `/data/processed/yyyy-mm-dd/data.parquet`. Inserts the transformed data into a SQLite database.


