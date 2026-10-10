from fastapi import HTTPException, status
from app.core.security import verify_password, create_access_token
from app.repositories.user_repository import UserRepository
from app.schemas.auth import TokenResponse

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def authenticate_user(self, username: str, password: str) -> TokenResponse:
        # 1. Cari user berdasarkan username melalui repository
        user = self.user_repo.get_by_username(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username atau password salah",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # 2. Verifikasi password dengan hash yang tersimpan
        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username atau password salah",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # 3. Cek apakah status user aktif
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Akun pengguna tidak aktif"
            )

        # 4. Generate JWT token
        access_token = create_access_token(data={"sub": user.username, "id": user.id})

        return TokenResponse(
            access_token=access_token,
            token_type="bearer"
        )