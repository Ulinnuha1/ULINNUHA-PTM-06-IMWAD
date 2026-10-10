from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.repositories.model_repository import ModelRepository
from app.services.prediction_service import PredictionService

router = APIRouter(prefix="/predictions", tags=["Predictions"])

def get_prediction_service(db: Session = Depends(get_db)) -> PredictionService:
    model_repo = ModelRepository(db)
    return PredictionService(model_repo)

@router.post("", response_model=PredictionResponse, status_code=status.HTTP_200_OK)
def predict(
    payload: PredictionRequest,
    service: PredictionService = Depends(get_prediction_service)
):
    return service.predict_class(payload)