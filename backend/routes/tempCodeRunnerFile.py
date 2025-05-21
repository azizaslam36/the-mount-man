# Add a new product
# @product_bp.route("/add", methods=["POST"])
# def add_product():
#     data = request.json
#     if not data.get("name") or not data.get("price") or not data.get("image"):
#         return jsonify({"error": "Missing required fields"}), 400
    
#     db.products.insert_one(data)
#     return jsonify({"message": "Product added successfully"}), 201

# # Delete a product
# @product_bp.route("/delete/<string:product_name>", methods=["DELETE"])
# def delete_product(product_name):
#     result = db.products.delete_one({"name": product_name})
#     if result.deleted_count == 0:
#         return jsonify({"error": "Product not found"}), 404
#     return jsonify({"message": "Product deleted successfully"}), 200
