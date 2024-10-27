from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import os
import secrets

# MongoDB connection
client = MongoClient("mongodb+srv://contactzcsco:Z3r0c0575k1ll%4066202@zcsproduction.zld0i.mongodb.net/?retryWrites=true&w=majority&appName=ZCSProduction")
db = client['NCCDatabase']
users_collection = db['users']

# User details
username = "adnan"
password = "password"  # Plain text password

# Generate hashed password
hashed_password = generate_password_hash(password)

# Insert user into the database
user_data = {
    'username': username,
    'password': hashed_password
}

# Insert user into MongoDB
try:
    users_collection.insert_one(user_data)
    print(f"User '{username}' added successfully!")
except Exception as e:
    print(f"Error adding user: {e}")

# Generate a random secret key
secret_key = secrets.token_hex(16)
print(f"Generated secret key: {secret_key}")

# Save secret key to a file (optional)
with open("secret_key.txt", "w") as f:
    f.write(secret_key)
    print("Secret key saved to 'secret_key.txt'")
