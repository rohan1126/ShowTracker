from flask import Flask, request, render_template, redirect, url_for
from AnilistPython import Anilist
from tmdbv3api import TMDb, TV
from tmdbv3api import Movie
from flask import Blueprint, render_template
tv_bp = Blueprint('tv', __name__)

@tv_bp.route('/search_tv', methods=['GET', 'POST'])
def search_tv():
    if request.method == 'POST':
        query = request.form['tv_query']
        tv = TV()
        search_results = tv.search(query)

        return render_template('tv_search_results.html', results=search_results)

    return render_template('tv_search_form.html')