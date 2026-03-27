from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict

class UserBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
