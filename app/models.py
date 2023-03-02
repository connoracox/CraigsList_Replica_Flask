from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    cars = db.relationship('Car', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def __str__(self):
        return f'User: {self.email}|{self.username}'
                    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(64))
    model = db.Column(db.String(64))
    year = db.Column(db.String(64))
    color = db.Column(db.String(64))
    price = db.Column(db.String(64))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Car {self. make}{self.model}>'