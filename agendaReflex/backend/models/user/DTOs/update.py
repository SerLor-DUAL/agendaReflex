# app/backend/models/user/DTOs/update.py

# Import necessary modules
from sqlmodel import Field                                 # Importing SQLModel for database operations
from typing import Optional                                # Importing Optional for type hints
from backend.models.user.DTOs.base import UserBase         # Importing UserBase

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# NOTE: This DTO (Data Transfer Object) defines the user update model used in the client-side, which includes the new password.
class UserUpdate(UserBase):
    password: Optional[str] = Field(None, min_length=6)     # Optional new password that will be encrypted before storing