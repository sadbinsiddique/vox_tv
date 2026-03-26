from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

# ==================== Authentication Schemas ====================
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: str = Field(default="user", pattern="^(admin|user)$")

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)
    current_password: Optional[str] = Field(None, min_length=1)
    role: Optional[str] = Field(None, pattern="^(admin|user)$")
    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool
    last_login: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)