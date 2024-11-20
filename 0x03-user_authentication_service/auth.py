#!/usr/bin/env python3
""" module to hash password """
import bcrypt
from db import DB
from user import User


class Auth:
    """
    Auth class to interact with the authentication database
    """
    def _hash_password(self, password: str) -> bytes:
        """ returns salted hashed password
        """
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            user_exists = self._db._session.query(User).filter_by(email=email).first()
            if user_exists:
                raise ValueError(f"User {email} already exists")
        except Exception as e:
            raise ValueError(f"error: {e}")
        
        hashed_password = self._hash_password(password)

        new_user = User(email=email,
                hashed_password=hashed_password)

        """ saving to database """
        self._db._session.add(new_user)
        self._db._session.commit()

        return new_user

