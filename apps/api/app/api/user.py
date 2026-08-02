from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    new_user = create_user(db, user)

    return UserResponse(
        id=new_user.id,
        email=new_user.email,
        username=new_user.username,
        is_active=new_user.is_active,
    )


@router.get("/", response_model=list[UserResponse])
def list_users(
    db: Session = Depends(get_db),
):
    users = get_all_users(db)

    return [
        UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            is_active=user.is_active,
        )
        for user in users
    ]


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        is_active=user.is_active,
    )