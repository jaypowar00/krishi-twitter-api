from app import app, init_db
from app.posts.models import Posts

if __name__ == '__main__':
    print('1')
    init_db()
    app.run(debug=True)
