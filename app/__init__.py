import os
from flask import Flask
from app.posts.routs import posts
from app.weather.routs import weather
from app.posts.models import post_db, Posts
app = Flask(__name__)

app.register_blueprint(posts)
app.register_blueprint(weather)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

post_db.init_app(app)
post_db.app = app
def create_app():
    print('2')
    post_db.create_all()
    return app
