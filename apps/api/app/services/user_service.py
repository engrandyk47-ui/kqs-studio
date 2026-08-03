from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hash_password(user.password),
        is_active=True,
        is_superuser=False,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()