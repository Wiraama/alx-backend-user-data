#!/usr/bin/env python3
""" module to hash password """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from flask import request


def _hash_password(password: str) -> bytes:
    """ returns salted hashed password
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


class Auth:
    """
    Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ ... """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"{email} already exists")

    def valid_login(self, email, password) ->bool:
        """ this function validate login
        """
        try:
            user = self._db.find_user_by(email=email)

            if user:
                if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                    return True
                else:
                    return False
        except Exception as e:
            return False
