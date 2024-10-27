#!/usr/bin/env python3

import bcrypt

# Hash the password
password = 'securepassword123'
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Define a user document with the hashed password
user_data = {
    'username': 'johndoe',
    'email': 'johndoe@example.com',
    'password': hashed_password.decode('utf-8')
}

# Insert the user document into the collection
result = users_collection.insert_one(user_data)
print(f'User inserted with ID: {result.inserted_id}')
