#!/usr/bin/env python3
""" authentication module """
from flask import request, Flask
from typing import List, TypeVar


class Auth:
    """ class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False path"""
        return False

    def authorization_header(self, request=None) -> str:
        """ return None fopr now """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return none for now """
        return None
