
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


def get_user_service(
    db: Session = Depends(get_db),
) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return service.create_user(user_data)


@router.get("", response_model=List[UserResponse])
def list_users(
    skip: int = 0,
    limit: int = 100,
    service: UserService = Depends(get_user_service),
    current_user=Depends(get_current_user),
):
    if not getattr(current_user, "is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Hanya admin yang dapat melihat daftar pengguna",
        )

    if skip < 0 or limit < 1 or limit > 100:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="skip harus >= 0 dan limit harus antara 1 sampai 100",
        )

    return service.list_users(skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
    current_user=Depends(get_current_user),
):
    is_admin = getattr(current_user, "is_admin", False)

    if user_id != current_user.id and not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Anda tidak memiliki akses ke data pengguna ini",
        )

    return service.get_user_by_id(user_id)
