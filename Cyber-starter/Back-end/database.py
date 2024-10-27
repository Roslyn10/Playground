#!/usr/bin/env python3 

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:8080/')  # Change the URI if using a remote server

# Create or switch to the 'user_database'
db = client['user_database']

# Create or switch to the 'users' collection
users_collection = db['users']

# Define a user document
user_data = {
    'username': 'johndoe',
    'email': 'johndoe@example.com',
    'password': 'securepassword123'  # Make sure to hash passwords in a real application!
}

# Insert the user document into the collection
result = users_collection.insert_one(user_data)

# Print the inserted ID
print(f'User inserted with ID: {result.inserted_id}')

