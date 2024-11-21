#!/usr/bin/env python3
""" module to hash password """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from flask import request
import uuid


def _hash_password(password: str) -> bytes:
    """ returns salted hashed password
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def _generate_auth() -> str:
    """ generate uuid
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ this function validate login
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)

            if user is not None:
                return bcrypt.checkpw(
                        password.encode('utf-8'),
                        user.hashed_password)
        except Exception as e:
            return False
        return False

