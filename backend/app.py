from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from database import db  # Import db from database.py

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
