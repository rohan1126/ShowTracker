from flask import Flask, request, render_template, redirect, url_for
from AnilistPython import Anilist
from tmdbv3api import TMDb, TV
from tmdbv3api import Movie
from flask import Blueprint, render_template
tmdb = TMDb()
tmdb.api_key = '4b83be6ffa6e7f0258bbf4d265901b3c'

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/search_movie', methods=['GET', 'POST'])
def search_movie():
    if request.method == 'POST':
        query = request.form['movie_query']
        movie = Movie()
        search_results = movie.search(query)

        return render_template('movie_search_results.html', results=search_results)

    return render_template('movie_search_form.html')