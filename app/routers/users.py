from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user, list_users

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

@router.get("", response_model=List[UserRead])
def list_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)

