#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token, jwt_required, JWTManager,
    get_jwt_identity)


app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'secured_key'


users = {
    "user1":
    {"username": "user1", "password": generate_password_hash("password"),
     "role": "user"},
    "admin1":
    {"username": "admin1", "password": generate_password_hash("password"),
     "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users \
       and check_password_hash(users.get(username), password):
        return username


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def access():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = data.get(username)

    if data and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "access denied"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
