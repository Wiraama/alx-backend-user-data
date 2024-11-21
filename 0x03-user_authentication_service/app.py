#!/usr/bin/env python3
from flask import Flask, jsonify, request
from auth import Auth
from user import User


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """  return jsonify
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['GET', 'POST'])
def users():
    """ takes user and register to db
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message": "missing email or password"}), 400

    try:
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"message": "email already registered"}), 400

        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 201
    except Exception as e:
        return jsonify({"message": f"error {str(e)} occurred"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
