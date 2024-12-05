import os
import csv
from collections import deque

# Initialize the deque for real-time sensor data
sensor_data = deque(maxlen=100)

# Set the path to the historical data file
HISTORICAL_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'historical_data_temp.txt')

def load_historical_data():
    historical_data = []
    try:
        with open(HISTORICAL_DATA_PATH, 'r') as file:
            reader = csv.reader(file)  # Use csv.reader instead of DictReader
            for row in reader:
                if len(row) == 2:  # Ensure there are exactly two columns
                    timestamp = row[0]  # First column is the timestamp
                    temperature = float(row[1])  # Second column is the temperature
                    historical_data.append({
                        'timestamp': timestamp,
                        'temperature': temperature,
                        'humidity': None  # You can set humidity to None or handle it accordingly
                    })
    except FileNotFoundError:
        print("Historical data file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return historical_data
