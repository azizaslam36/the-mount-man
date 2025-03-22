from pymongo import MongoClient
from werkzeug.security import generate_password_hash

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["the_mount_man"]
admins = db["admins"]

# Create an admin user
admin_data = {
    "email": "admin@example.com",  # Change this to your admin email
    "password": generate_password_hash("admin123")  # Change this password
}

# Insert the admin into the database
admins.insert_one(admin_data)
print("✅ Admin created successfully!")
