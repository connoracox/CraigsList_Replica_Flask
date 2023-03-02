from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, SignInForm, CarForm
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()
    if form.validate_on_submit():
        make= form.make.data
        model= form.model.data
        year= form.year.data
        color= form.color.data
        price= form.price.data
        c = User(make=make,model=model,year=year,color=color,price=price)
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
         flash(f'{form.username} successfully signed in!')
         return redirect('/')
    return render_template('log_in.jinja', sign_in_form = form)

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
        #  db.session.add(u)
        #  db.session.commit()
        u.commit()
        flash(f'Request to register {username} successful!')
        return redirect('/')
    return render_template('register.jinja', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.jinja')