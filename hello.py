from flask import Flask
from flask import request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return F'{user_agent}'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello {name}!</h1>'

if __name__ == '__main__':
    manager.run()
