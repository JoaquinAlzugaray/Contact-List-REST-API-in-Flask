from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=False)
    # groups = db.Column(db.Integer, foreing_key) averiguar como hacer m:m

    def __repr__(self):
        return '<Contact %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email":self.email,
            "address": self.address,
            "phone": self.phone
            # do not serialize the password, its a security breach
        }

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), unique=True, nullable=False)
    contacts = db.Column(db.String(350), unique=False, nullable=False)
    # contacts = db.Column(db.Integer, foreing_key) averiguar como hacer m:m

    def __repr__(self):
        return '<Group %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "group_name": self.group_name,
            "contacts": self.contacts
        }