from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user, list_users, get_user, update_user, delete_user

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

@router.get("/{user_id}", response_model=UserRead)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
def update_user_endpoint(user_id: int, payload: UserCreate, db: Session = Depends(get_db)):
    try:
        user = update_user(db, user_id, payload)
    except LookupError:
        raise HTTPException(status_code=404, detail="User not found")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    try:
        delete_user(db, user_id)
    except LookupError:
        raise HTTPException(status_code=404, detail="User not found")
    return None

