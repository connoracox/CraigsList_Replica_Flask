from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, SignInForm, CarForm
from app.models import User, Car
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = CarForm()
    if form.validate_on_submit():
        make= form.make.data
        model= form.model.data
        year= form.year.data
        color= form.color.data
        price= form.price.data
        c = Car(make=make,model=model,year=year,color=color,price=price)
        #  db.session.add(u)
        #  db.session.commit()
        c.commit()
        flash(f'Car: {make} {model} successfully added!')
        return redirect('/')
    return render_template('index.jinja', car_form=form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        password_match = User.query.filter_by(password_hash=password).first()
        if not user_match or not password_match:
            flash(f'Username and/or Password was incorrect. Try again!')
            return redirect('/log_in')
        flash(f'{username} successfully signed in!')
        login_user(user_match)
        return redirect('/')
    return render_template('log_in.jinja', sign_in_form = form)

@app.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username= form.username.data
        email= form.email.data
        password= form.password.data
        first_name= form.first_name.data
        last_name= form.last_name.data
        u = User(username=username,email=email,password_hash=password,first_name=first_name,last_name=last_name)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists. Try again!')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exists. Try again!')
            return redirect('/register')
        else:
            u.commit()
            flash(f'Request to register {username} successful.')
            return redirect('/')
    return render_template('register.jinja', form = form)

@app.route('/blog')
def blog():
    return render_template('blog.jinja')