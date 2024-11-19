#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


""" initializing """
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    """ user class of storange """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    hashed_password = db.Column(db.String(250), nullable=False)
    session_id = db.Column(db.String(250), nullable=True)
    reset_token = db.Column(db.String(250), nullable=True)
