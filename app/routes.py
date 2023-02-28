from flask import render_template
from app import app

@app.route('/')
def index():
    cdn={
        'locations':('restaurant', 'brewery'),
        'foods':['pizza', 'tacos', 'french fries', 'nachos']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/log_in')
def log_in():
    return render_template('log_in.jinja')

@app.route('/register')
def register():
    return render_template('register.jinja')

@app.route('/blog')
def blog():
    return render_template('blog.jinja')