from flask import Blueprint, render_template
from flask import Flask, request, render_template, redirect, url_for
from AnilistPython import Anilist

anime_bp = Blueprint('anime', __name__)

@anime_bp.route('/search_anime', methods=['GET', 'POST'])
def search_anime():
    anilist = Anilist()
    if request.method == 'POST':
        user_show = request.form['show_name']
        data = anilist.get_anime(user_show)
        if data:
            return render_template('anime_info.html', data=data)
        else:
            return "Anime not found. Please try another title."
    return render_template('search_form.html')