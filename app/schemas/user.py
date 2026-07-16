from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserCreate(BaseModel):
    """Payload for POST /auth/signup"""
    full_name: str = Field(..., min_length=2, max_length=100, examples=["Jane Doe"])
    email: EmailStr = Field(..., examples=["jane@example.com"])
    password: str = Field(..., min_length=8, max_length=128, examples=["StrongPass123!"])


class UserLogin(BaseModel):
    """Payload for POST /auth/login"""
    email: EmailStr
    password: str


class UserOut(BaseModel):
    """What we return to clients - never includes hashed_password."""
    model_config = ConfigDict(from_attributes=True)

    id: str
    full_name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str | None = None


class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None
    type: str | None = None  # "access" or "refresh"
