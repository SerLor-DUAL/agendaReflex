# app/backend/models/user/DTOs/login.py

# Import necessary modules
from pydantic import Field                                 # Importing SQLModel for database operations
from typing import Optional                                # Importing Optional for type hints
from .base import UserBase                                 # Importing UserBase

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# NOTE: This DTO (Data Transfer Object) defines the user login model used in the client-side, which includes the user password.
class UserLogin(UserBase):
    password: Optional[str] = Field(None, min_length=6)