import os
from flask import Flask
from app.posts.routs import posts
from app.weather.routs import weather
from app.posts.models import post_db, Posts
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)

app.register_blueprint(posts)
app.register_blueprint(weather)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)


post_db.init_app(app)
with app.app_context():
    post_db.create_all()

def create_app():
    post_db.init_app(app)
    with app.app_context():
        post_db.create_all()
    return app
