from flask import Blueprint, jsonify
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
