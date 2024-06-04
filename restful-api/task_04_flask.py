#!/usr/bin/python3
"""import Flask, jsonify  and request modules"""
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():

    # we are fetching the data given
    user_data = request.get_json()

    username = user_data.get("username")

    # we check if username is given
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # we create the new user
    users[username] = user_data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run()
