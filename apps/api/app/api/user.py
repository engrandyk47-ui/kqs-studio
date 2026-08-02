from fastapi import APIRouter

from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return UserResponse(
        id=1,
        email=user.email,
        username=user.username,
        is_active=True,
    )