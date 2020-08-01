from datetime import datetime

from flask import Flask
from flask import request
from flask import render_template

from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)

moment = Moment(app)

manager = Manager(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/index.html')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello {name}!</h1>'

if __name__ == '__main__':
    manager.run()
