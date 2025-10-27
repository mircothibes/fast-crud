from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(name=user_in.name.strip(), email=user_in.email.lower()).strip()
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


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user_in: UserCreate) -> User:
    user = get_user(db, user_id)
    if not user:
        raise LookupError("User not found")
    user.name = user_in.name.strip()
    user.email = user_in.email.lower().strip()
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> None:
    user = get_user(db, user_id)
    if not user:
        raise LookupError("User not found")
    db.delete(user)
    db.commit()





