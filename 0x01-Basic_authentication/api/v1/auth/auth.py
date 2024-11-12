#!/usr/bin/env python3
""" authentication module """
from flask import request, Flask
from typing import List, TypeVar


class Auth:
    """ class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        args: path, excluded_path
        return: boolean"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        path = path if path.endswith('/') else path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ return None fopr now """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return none for now """
        return None
