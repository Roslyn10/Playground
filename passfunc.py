import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes a plain text password."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("UTF-8"), salt)

def is_valid(password: str, hash_password: bytes) -> bool:
    """Validates that a provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode("UTF-8"), hash_password)

# Example usage
plain_password = "my_secret_password"
hashed = hash_password(plain_password)  # Hash the password

# Validate the password against the hashed version
if is_valid(plain_password, hashed):
    print("Password is valid!")
else:
    print("Invalid password!")

