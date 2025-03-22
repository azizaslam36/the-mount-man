from flask import Flask 
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from database import db  # Import db from database.py
from routes.product_routes import product_bp
from routes.auth_routes import auth_bp

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
 # Allow frontend to access backend

# Debugging to check if .env is loaded correctly
MONGO_URI = os.getenv("MONGO_URI")
print("Mongo URI:", MONGO_URI)
if not MONGO_URI:
    print("Error: MONGO_URI is not set. Check your .env file.")

client = MongoClient(MONGO_URI)
db = client["mountman"]

@app.route("/")
def home():
    return {"message": "Backend is running!"}

# Import routes AFTER defining `db` to avoid circular imports
from routes.product_routes import product_bp
from routes.auth_routes import auth_bp

# Register API routes
app.register_blueprint(product_bp, url_prefix="/api/products")
app.register_blueprint(auth_bp, url_prefix="/api/auth")

if __name__ == "__main__":
    app.run(debug=True, port=5000)


from flask import Flask, request, jsonify, session, redirect, url_for
from pymongo import MongoClient
from werkzeug.security import check_password_hash
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this
CORS(app)  # Allow frontend requests

client = MongoClient("mongodb://localhost:27017/")
db = client["the_mount_man"]
admins = db["admins"]

@app.route("/api/admin/login", methods=["POST"])
def admin_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    admin = admins.find_one({"email": email})
    if admin and check_password_hash(admin["password"], password):
        session["admin_logged_in"] = True
        return jsonify({"message": "Login successful", "redirect": "/admin.html"})
    else:
        return jsonify({"message": "Invalid email or password"}), 401

@app.route("/api/admin/logout", methods=["GET"])
def admin_logout():
    session.pop("admin_logged_in", None)
    return jsonify({"message": "Logged out successfully", "redirect": "/admin-login.html"})

if __name__ == "__main__":
    app.run(debug=True)
