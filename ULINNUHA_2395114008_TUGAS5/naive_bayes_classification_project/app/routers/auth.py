from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    user_repo = UserRepository(db)
    return AuthService(user_repo)

@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    payload: LoginRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.authenticate_user(payload.username, payload.password)