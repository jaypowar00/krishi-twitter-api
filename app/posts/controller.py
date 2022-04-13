import math
import os
from flask import make_response, request
from app.posts.models import Posts, post_db
from datetime import timedelta, datetime
import psycopg2
from pretty import date


def create_post():
    """
    This function recieves an POST request from user which consists of message, long & lan values.
    using these values from the request we are creating a new post in the database.
    """
    if request.data and request.json:
        try:
            jsn = request.json
            if not ('message' in jsn and 'location' in jsn and 'x' in jsn['location'] and 'y' in jsn['location']):
                res = make_response(
                    {
                        'status': False,
                        'message': 'fields missing in the request (message, location)'
                    }
                )
            else:
                message = jsn['message']
                location = jsn['location']
                post = Posts(message=message, point='SRID=4326;POINT('+location["x"]+' '+location["y"]+')', created=datetime.utcnow())
                post_db.session.add(post)
                post_db.session.commit()
            res = make_response(
                {
                    'status': True,
                    'message': 'successfully created post'
                }
            )
            res.mimetype = 'application/json'
            return res
        except Exception as e:
            print('error in post cration')
            print(e)
            res = make_response(
                {
                    'status': False,
                    'message': 'Something went wrong! ('+e+')'
                }
            )
            res.mimetype = 'application/json'
            return res

def get_posts():
    """
    This function retrieves all the posts from our database and sends back as response to the user.
    """
    location = {}
    page = None
    params = False
    if 'x' in request.args and 'y' in request.args:
        params = True
        location['x'] = request.args['x']
        location['y'] = request.args['y']
        page = request.args['page'] if 'page' in request.args else 1
    if (params) or (request.data and request.json):
        if not params:
            jsn = request.json
            if not ('location' in jsn and 'x' in jsn['location'] and 'y' in jsn['location']):
                res = make_response(
                    {
                        'status': False,
                        'message': 'please provide location in request'
                    }
                )
                res.mimetype = 'application/json'
                return res
            location = jsn['location']
            page = jsn['page'] if 'page' in jsn else 1
            # mytime = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S.%f%z")
        try:
            conn = psycopg2.connect(database=os.getenv("K_DATABASE"), user=os.getenv("K_USER"), password=os.getenv("K_PASSWORD"), host=os.getenv("K_HOST"), port=os.getenv("K_PORT"))
            cur = conn.cursor()
            cur.execute(f"""
            SELECT json_agg(
                row_to_json(
                    (
                        SELECT ColumnName 
                        FROM (SELECT t.pid, t.message, t.created, t.dist)
                        AS
                        ColumnName (pid, message, created, dist)
                    )
                )
            ) FROM 
            (
                SELECT p.pid,  p.message, p.created,
                ST_Transform(p.point, 4326),
                p.point <-> 'SRID=4326;POINT({location['x']} {location['y']})'::geometry AS dist
                FROM posts p
                ORDER BY dist
                LIMIT 10 OFFSET {(page-1)*10}
            ) t;
            """)
            all_posts = cur.fetchall()[0][0]
            if all_posts:
                for one_post in all_posts:
                    mytime = datetime.strptime(one_post['created'], "%Y-%m-%dT%H:%M:%S.%f%z")
                    # mytime += timedelta(hours=5, minutes=30)
                    mytime = datetime.astimezone(mytime).replace(tzinfo=None)
                    print('----')
                    print(date(mytime))
                    temp = str(date(mytime))
                    if temp not in ["now", "a minute ago", "an hour ago", "yesterday", "day before", "last week", "last month", 
                    "in a minute", "in an hour", "tomorrow", "day after", "next week", "next month"]:
                        one_post['created'] = str(math.floor(int(float(str(date(mytime)).split()[0]))))+" "+" ".join((date(mytime)).split()[1:])
                    else:
                        one_post['created'] = temp
            cur.close()
            n = Posts.query.count()
            res = make_response(
                {
                    'status': True,
                    'total_tweets': n,
                    'page_tweets': len(all_posts) if all_posts else 0,
                    'tweets': all_posts,
                    'current_page': page,
                    'prev_page': page-1 if page>1 else None,
                    'next_page': math.ceil(n/10) if math.ceil(n/10)>page else None,
                }
            )
        except psycopg2.OperationalError:
            return 500,{'Server Error':'Database Error'}
        except psycopg2.errors.UndefinedColumn:
            return 500,{'Server Error':'Invalid Orderby'}
        except psycopg2.errors.SyntaxError:
            return 500,{'Server Error':'Invalid Search String'}
        except psycopg2.errors.AmbiguousFunction:
            return 500,{'Server Error':'Invalid Search String'}
    else:
        res = make_response(
                {
                    'status': False,
                    'message': 'please provide location in request'
                }
            )
    res.mimetype = 'application/json'    
    return res
