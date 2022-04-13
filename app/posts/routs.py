from flask import Blueprint, make_response

from app.posts.controller import create_post, get_posts

posts = Blueprint('posts', __name__, url_prefix='/posts')

posts.add_url_rule("/create", "create", create_post, methods=['POST'])
posts.add_url_rule("/", "getposts", get_posts, methods=['GET'])
