from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, SignInForm, CarForm

@app.route('/')
def index():
    form = CarForm()
    return render_template('index.jinja', car_form=form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/log_in')
def log_in():
    form = SignInForm()
    return render_template('log_in.jinja', sign_in_form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
         flash(f'Request to register {form.username} successful!')
         return redirect('/')
    return render_template('register.jinja', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.jinja')