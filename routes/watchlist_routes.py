from flask import Flask, request, render_template, redirect, url_for
from AnilistPython import Anilist
from tmdbv3api import TMDb, TV
from tmdbv3api import Movie
from flask import Blueprint, render_template


import sqlite3

watchlist_bp = Blueprint('watchlist', __name__)

@watchlist_bp.route('/watchlist', methods=['GET', 'POST'])

def get_db_connection():
    connection = sqlite3.connect('watchlist.db')
    connection.row_factory = sqlite3.Row
    return connection

@watchlist_bp.route('/add_watchlist/<show_name>', methods=['GET'])
def add_watchlist(show_name):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT show_name FROM watchlist WHERE show_name = ?", (show_name,))
    existing_show = cursor.fetchone()

    if existing_show:
        connection.close()
        message = f"{show_name} is already in your watchlist. <a href='/'>Return to Home</a>"
    else:
        cursor.execute("INSERT INTO watchlist (show_name) VALUES (?)", (show_name,))
        connection.commit()
        connection.close()
        message = f"{show_name} has been added to your watchlist. <a href='/'>Return to Home</a>"

    return message

@watchlist_bp.route('/view_watchlist', methods=['GET'])
def view_watchlist():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT show_name FROM watchlist")
    watchlist = [row['show_name'] for row in cursor.fetchall()]

    connection.close()

    # Log the watchlist content
    print("Watchlist:", watchlist)

    return render_template('watchlist.html', watchlist=watchlist)


@watchlist_bp.route('/remove_watchlist/<show_name>', methods=['GET'])
def remove_watchlist(show_name):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM watchlist WHERE show_name = ?", (show_name,))
    connection.commit()
    connection.close()

    return f"{show_name} has been removed from your watchlist. <a href='/watchlist'>View Watchlist</a>"

