#!/usr/bin/env python3

from pymongo import MongoClient
import bcrypt

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:8080/')
db = client['user_database']
users_collection = db['users']

# Function to create a user
def create_user(username, email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        'username': username,
        'email': email,
        'password': hashed_password.decode('utf-8')
    }
    result = users_collection.insert_one(user_data)
    print(f'User inserted with ID: {result.inserted_id}')

# Insert sample users
create_user('johndoe', 'johndoe@example.com', 'securepassword123')
create_user('janedoe', 'janedoe@example.com', 'password321')

