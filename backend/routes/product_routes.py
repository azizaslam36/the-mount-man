from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["mountman"]

product_bp = Blueprint("product_routes", __name__)

@product_bp.route("/")
def get_products():
    return jsonify({"message": "Products endpoint is working!"})

# Sample route to fetch all products from MongoDB
@product_bp.route("/all", methods=["GET"])
def get_all_products():
    products = list(db.products.find({}, {"_id": 0}))  # Get all products
    return jsonify(products)


product_bp = Blueprint("products", __name__)

# Fetch all products
@product_bp.route("/", methods=["GET"])
def get_products():
    products = list(db.products.find({}, {"_id": 0}))  # Exclude MongoDB `_id` field
    return jsonify(products)

# Add a new product
@product_bp.route("/add", methods=["POST"])
def add_product():
    data = request.json
    if not data.get("name") or not data.get("price") or not data.get("image"):
        return jsonify({"error": "Missing required fields"}), 400
    
    db.products.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201

# Delete a product
@product_bp.route("/delete/<string:product_name>", methods=["DELETE"])
def delete_product(product_name):
    result = db.products.delete_one({"name": product_name})
    if result.deleted_count == 0:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted successfully"}), 200
