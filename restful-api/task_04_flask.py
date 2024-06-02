#!/usr/bin/python3
"""import Flask, jsonify  and request modules"""
from flask import Flask, jsonify, request


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
def user_to_find(username):
    if username in users:
        return jsonify(users[username])
    else:
        error = {"error": "User not found"}
        return jsonify(error)


@app.route("/add_user", methods=["POST"])
def add_user():

    user_data = request.get_json()

    username = user_data.get("username")

    users[username] = user_data
    return jsonify({
        "message": "User added",
        "user": user_data
    })


if __name__ == "__main__":
    app.run()
