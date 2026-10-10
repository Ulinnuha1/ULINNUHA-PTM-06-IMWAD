from typing import List
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_data: UserCreate) -> UserResponse:
        if self.user_repo.get_by_username(user_data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username sudah terdaftar"
            )
        if self.user_repo.get_by_email(user_data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email sudah terdaftar"
            )
        
        hashed_pw = get_password_hash(user_data.password)
        user = self.user_repo.create(user_data, hashed_pw)
        return UserResponse.model_validate(user)

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pengguna tidak ditemukan"
            )
        return UserResponse.model_validate(user)

    def list_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        users = self.user_repo.get_all(skip=skip, limit=limit)
        return [UserResponse.model_validate(u) for u in users]