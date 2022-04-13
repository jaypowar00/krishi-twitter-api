import os
from flask import Flask
from app.posts.routs import posts
from app.weather.routs import weather
from app.posts.models import post_db, Posts
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
db = SQLAlchemy(app)

app.register_blueprint(posts)
app.register_blueprint(weather)

print('[+] db uri:', end=' ')
print(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)

print('[+] in __init__ file')

post_db.init_app(app)
post_db.create_all()
def create_app():
    print('2')
    post_db.init_app(app)
    post_db.create_all()
    print('[+] create app ended!')
    return app
