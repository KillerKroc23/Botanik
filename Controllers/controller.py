from flask import Blueprint, render_template, jsonify
import os

main_bp = Blueprint('main_controller', __name__)

@main_bp.route('/')
def home_func():
    return render_template('home.html')

@main_bp.route('/historical')
def historicaldata_func():
    return render_template('historicaldata.html')

@main_bp.route('/get-historical-data')
def get_historical_data():
    humidity_data = []
    temp_data = []
    timestamps = set()

    # Read humidity data
    humidity_file_path = r"C:\Users\chris\Desktop\Lab04\Data\historical_data_humidity.txt"
    try:
        with open(humidity_file_path, "r") as humidity_file:
            for line in humidity_file:
                timestamp, humidity = line.strip().split(',')
                humidity_data.append({
                    'timestamp': timestamp,
                    'humidity': float(humidity)
                })
                timestamps.add(timestamp)
    except FileNotFoundError:
        print(f"Could not find humidity file at: {humidity_file_path}")
    except Exception as e:
        print(f"Error reading humidity file: {str(e)}")

    # Read temperature data
    temp_file_path = r"C:\Users\chris\Desktop\Lab04\Data\historical_data_temp.txt"
    try:
        with open(temp_file_path, "r") as temp_file:
            for line in temp_file:
                timestamp, temperature = line.strip().split(',')
                temp_data.append({
                    'timestamp': timestamp,
                    'temperature': float(temperature)
                })
                timestamps.add(timestamp)
    except FileNotFoundError:
        print(f"Could not find temperature file at: {temp_file_path}")
    except Exception as e:
        print(f"Error reading temperature file: {str(e)}")

    # Sort timestamps
    timestamps = sorted(list(timestamps))

    # Create response data
    response_data = {
        'timestamps': timestamps,
        'humidities': [next((item['humidity'] for item in humidity_data if item['timestamp'] == ts), None) for ts in timestamps],
        'temperatures': [next((item['temperature'] for item in temp_data if item['timestamp'] == ts), None) for ts in timestamps]
    }

    return jsonify(response_data)

@main_bp.route('/LiveData')
def livedata_func():
    return render_template('livedata.html')

@main_bp.route('/about')
def about_func():
    return render_template('about.html')

@main_bp.route('/contact')
def contact_func():
    return render_template('contact.html')