from app import app, create_app
from app.posts.models import Posts

if __name__ == '__main__':
    create_app()
    app.run(debug=True)
