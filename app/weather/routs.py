from flask import Blueprint

from app.weather.controller import get_weather

weather = Blueprint('weather', __name__, url_prefix='/weather')

weather.add_url_rule("/", "get-weather", get_weather, methods=['GET'])