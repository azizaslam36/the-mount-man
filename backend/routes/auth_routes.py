from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from database import db  # Import db from database.py

auth_bp = Blueprint("auth_bp", __name__)
bcrypt = Bcrypt()

# Admin Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    admin = db.users.find_one({"username": data["username"]})

    if not admin or not bcrypt.check_password_hash(admin["password"], data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=admin["username"])
    return jsonify({"token": token})
