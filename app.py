from flask import Flask, redirect, url_for, session, request
from datetime import datetime, timedelta
import json
from collections import deque

from Controllers.controller import main_bp
from Controllers.auth import auth_bp
from config import Config
from Data.data_store import sensor_data

app = Flask(__name__)
app.config.from_object(Config)
app.permanent_session_lifetime = timedelta(minutes=1)  # Session expires when browser closes
app.secret_key = 'your-secret-key-here'  # Add a secret key

# Create a deque to store sensor data
sensor_data = deque(maxlen=100)

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

# Only check for login on the home route
@app.before_request
def check_login():
    session.permanent = False
    if request.endpoint == 'main_controller.home_func' and 'user' not in session:
        return redirect(url_for('auth_controller.login'))

# MQTT callback
def on_message(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode())
        payload['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sensor_data.append(payload)
    except Exception as e:
        print(f"Error processing message: {e}")

if __name__ == '__main__':
    app.run(debug=True)