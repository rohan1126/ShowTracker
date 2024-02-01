from flask import Flask
from flask import Flask, render_template
from routes.anime_routes import anime_bp
from routes.character_routes import character_bp
from routes.movie_routes import movie_bp
from routes.tv_routes import tv_bp
from routes.watchlist_routes import watchlist_bp
from routes.login_route import login_bp

app = Flask(__name__)

app.register_blueprint(anime_bp)
app.register_blueprint(character_bp)
app.register_blueprint(movie_bp)
app.register_blueprint(tv_bp)
app.register_blueprint(watchlist_bp)

@app.route('/')
def homepage():
    return render_template('homepage.html')
if __name__ == '__main__':
    app.run(debug=True)
