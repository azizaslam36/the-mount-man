from flask import Flask, send_from_directory, request, jsonify, session
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from werkzeug.security import check_password_hash,generate_password_hash

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow frontend access

# Set Flask secret key for sessions
app.secret_key = os.getenv("SECRET_KEY", "your_secret_key")  # Keep in .env

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
if not MONGO_URI:
    print("Error: MONGO_URI is not set. Check your .env file.")
client = MongoClient(MONGO_URI)
db = client["the_mount_man"]
admins = db["admins"]

# ✅ Serve index.html from frontend folder
@app.route("/")
def serve_frontend():
    return send_from_directory("../frontend", "index.html")

# ✅ Serve static frontend files (CSS, JS, Images)
@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("../frontend", path)

# ✅ Admin Login Route
@app.route("/api/admin/login", methods=["POST"])
def admin_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    admin = admins.find_one({"email": email})
    if admin and check_password_hash(admin["password"], password):  # Compares hashed password
        session["admin_logged_in"] = True
        return jsonify({"message": "Login successful", "redirect": "/admin.html"})
    else:
        return jsonify({"message": "Invalid email or password"}), 401

# Admin details (Change these before running)
admin_email = "admin@example.com"  # Change this email
admin_password = "admin123"  # Change this password

# Hash the password
hashed_password = generate_password_hash(admin_password)

# Insert into MongoDB
admin_data = {
    "email": admin_email,
    "password": hashed_password  # Store the hashed password
}

# Check if admin already exists
existing_admin = admins.find_one({"email": admin_email})
if existing_admin:
    print("Admin already exists!")
else:
    admins.insert_one(admin_data)
    print("Admin added successfully!")


# ✅ Admin Logout Route
@app.route("/api/admin/logout", methods=["GET"])
def admin_logout():
    session.pop("admin_logged_in", None)
    return jsonify({"message": "Logged out successfully", "redirect": "/admin-login.html"})

# ✅ Import routes AFTER defining `db` to avoid circular imports
from routes.product_routes import product_bp
from routes.auth_routes import auth_bp

# ✅ Register API routes
app.register_blueprint(product_bp, url_prefix="/api/products")
app.register_blueprint(auth_bp, url_prefix="/api/auth")

# ✅ Run the Flask server
if __name__ == "__main__":
    app.run(debug=True, port=5000)
