#!/usr/bin/env python3
""" user model """
from flask import Flask
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


""" initializing """
app = Flask(__name__)
Base = declarative_base()
DATABASE_URI = 'sqlite:///users.db'

class User(Base):
    """ user class of storange """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
