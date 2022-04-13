import os
from flask import request
import requests

def get_weather():
    location = {}
    params = False
    if 'x' in request.args and 'y' in request.args:
        location['x'] = request.args['x']
        location['y'] = request.args['y']
        params = True
    if request.data and request.json:
        if not params:
            jsn = request.json
            if 'location' in jsn and 'x' in jsn['location'] and 'y' in jsn['location']:
                location = jsn['location']
        res = requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+location['x']+'&lon='+location['y']+'&appid='+os.getenv('WEATHER_API_KEY')).json()
        res['status'] = True
        return res
            
