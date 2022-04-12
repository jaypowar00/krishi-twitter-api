from flask import Blueprint, make_response

weather = Blueprint('weather', __name__, url_prefix='/weather')

@weather.route('/')
def index():
    res = make_response({'status': True, 'message': 'testing weather...'})
    res.mimetype = 'application/json'
    return res
