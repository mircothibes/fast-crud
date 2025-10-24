from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(name=user_in.name, email=user_in.email)
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")
    db.refresh(user)
    return user

def list_users(db: Session) -> List[User]:
    return db.query(User).order_by(User.id.asc()).all()

