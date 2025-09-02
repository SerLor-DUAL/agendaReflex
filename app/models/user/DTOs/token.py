# app/backend/models/user/DTOs/token.py
from pydantic import BaseModel

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class MessageResponse(BaseModel):
    message: str
    

class RefreshResponse(BaseModel):
    message: str
    user_id: int
    
