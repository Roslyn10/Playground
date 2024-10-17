#!/usr/bin/env python3

import bcrypt

def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates the provided password matches the hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

