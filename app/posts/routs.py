from flask import Blueprint, make_response

posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/')
def index():
    res = make_response({'status': True, 'message': 'testing posts...'})
    res.mimetype = 'application/json'
    return res
