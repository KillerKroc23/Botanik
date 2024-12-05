from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_controller', __name__)

# Configure users with default credentials
users = {
    "admin": generate_password_hash("botanik2024")
}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Check if user is already logged in
    if 'user' in session:
        return redirect(url_for('main_controller.home_func'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Login attempt with username: {username}")  # Debug print

        if username in users and check_password_hash(users[username], password):
            session.clear()
            session['user'] = username
            print("Login successful")  # Debug print
            return redirect(url_for('main_controller.home_func'))

        print("Login failed")  # Debug print
        flash('Invalid username or password')
        return redirect(url_for('auth_controller.login'))

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_controller.login'))