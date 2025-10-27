from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # pydantic v2: allows ORM objects

