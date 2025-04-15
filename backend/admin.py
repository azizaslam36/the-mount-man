# from pymongo import MongoClient
# from werkzeug.security import generate_password_hash

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["the_mount_man"]
# admins = db["admins"]

# # Create an admin user
# admin_data = {
#     "email": "admin@example.com",  # Change this to your admin email
#     "password": generate_password_hash("admin123")  # Change this password
# }

# # Insert the admin into the database
# admins.insert_one(admin_data)
# print("✅ Admin created successfully!")

from pymongo import MongoClient
from werkzeug.security import generate_password_hash

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Change if using a different database URL
db = client["the_mount_man"]  # Your database name
admins = db["admins"]  # Collection for admins

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