# app/backend/models/user/DTOs/base.py

# Import necessary modules
from pydantic import BaseModel, Field            # Importing pydantic for data validation and serialization


# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# NOTE: This DTO (Data Transfer Object) defines the base user model used in the client-side.
        # It includes only the common fields we want to expose, not the full database model.
class UserBase(BaseModel):
        nickname: str = Field(..., max_length=100)  # User's nickname

        # ---------------------------------------------------------------------------------------------------------------------------------------------------- #

        # NOTE: The Config class is used to configure the model behavior.
        class Config:
                from_attributes = True  # Enables compatibility with ORM models, allowing the model to be used with SQLModel and Pydantic.
                
# ---------------------------------------------------------------------------------------------------------------------------------------------------- #