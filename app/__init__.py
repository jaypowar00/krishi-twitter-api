from flask import Flask
from .posts.routs import posts
from .weather.routs import weather

app = Flask(__name__)

app.register_blueprint(posts)
app.register_blueprint(weather)
