from flask import Blueprint, render_template
from flask import Flask, request, render_template, redirect, url_for
from AnilistPython import Anilist

character_bp = Blueprint('character', __name__)

@character_bp.route('/search_character', methods=['GET', 'POST'])
def search_character():
    anilist = Anilist()
    if request.method == 'POST':
        user_character = request.form['character_name']
        data = anilist.get_character(user_character)
        if data:
            return render_template('character_info.html', data=data)
        else:
            return "Character not found. Please try another name."
    return render_template('search_character_form.html')