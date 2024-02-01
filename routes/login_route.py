from flask import Flask, request, render_template, redirect, url_for
from AnilistPython import Anilist
from tmdbv3api import TMDb, TV
from tmdbv3api import Movie
import os
from flask import Blueprint, render_template


import sqlite3

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])

def create_user_database(username, password):
    db_file = f"{username}.db"

    if os.path.exists(db_file):
        return "Username already exists."

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS watchlist (
            movie_title TEXT,
            release_date TEXT,
            genre TEXT
        )
    """)

    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_name TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (user_name, password) VALUES (?, ?)", (username, password))

    connection.commit()
    connection.close()
    return "User created successfully."

def login(username, password):
    db_file = f"{username}.db"
    if not os.path.exists(db_file):
        return "Login failed. User not found."

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("SELECT password FROM users WHERE user_name=?", (username,))
    stored_password = cursor.fetchone()
    connection.close()

    if stored_password and stored_password[0] == password:
        return "Login successful"
    return "Login failed"

from flask import Blueprint, render_template, request, redirect, url_for

login_bp = Blueprint('login', __name__)

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = create_user_database(username, password)
        return result

    return render_template('register.html')  # Create an HTML template for user registration

@login_bp.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = login(username, password)
        return result

    return render_template('login.html')  # Create an HTML template for user login
