#!/usr/bin/env python3
""" module to hash password """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ returns salted hashed password
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password
