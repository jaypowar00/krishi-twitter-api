from app import app, create_app
from app.posts.models import Posts

print('[+] in run.py file')
if __name__ == '__main__':
    app.create_app()
    app.run(debug=True)
