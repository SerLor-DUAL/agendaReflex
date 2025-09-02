# app/backend/utils/hashing.py

# Import necessary modules
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# NOTE: This class handles password hashing and verification 
class HashHandler:

    def __init__(self):
        # Initialize the password hashing context
        self.ph = PasswordHasher()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------- #

    # Hash a plain password using argon2
    def hash_password(self, password: str) -> str:
        return self.ph.hash(password)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------- #

    # Verifies a plain password against a hashed password
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        try:
            return self.ph.verify(hashed_password, plain_password)
        except VerifyMismatchError:
            return False
    

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# Create an instance of HashHandler to use throughout the app
hash_handler = HashHandler()