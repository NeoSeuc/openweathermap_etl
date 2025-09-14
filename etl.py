from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_weather_data
from src.analytics import run_queries

def main():
    # Kiev region coordinates
    raw_file, raw_file_path = extract_weather_data(50.450001, 30.523333)
    processed_file = transform_weather_data(raw_file)
    load_weather_data(processed_file)
    run_queries()

if __name__ == "__main__":
    main()
