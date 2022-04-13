from sqlalchemy.sql import func
from geoalchemy2.types import Geometry
from flask_sqlalchemy import SQLAlchemy

post_db = SQLAlchemy()
class Posts(post_db.Model):
    __tablename__ = "posts"
    pid = post_db.Column(post_db.Integer, primary_key=True)
    message = post_db.Column(post_db.Text())
    point = post_db.Column(Geometry(geometry_type='POINT'))
    created = post_db.Column(post_db.DateTime(timezone=True), server_default=func.utcnow())
