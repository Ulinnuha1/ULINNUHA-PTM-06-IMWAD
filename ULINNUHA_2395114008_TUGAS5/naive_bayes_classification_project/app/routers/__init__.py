from fastapi import APIRouter
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.datasets import router as datasets_router
from app.routers.models_ml import router as models_ml_router
from app.routers.predictions import router as predictions_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(datasets_router)
api_router.include_router(models_ml_router)
api_router.include_router(predictions_router)