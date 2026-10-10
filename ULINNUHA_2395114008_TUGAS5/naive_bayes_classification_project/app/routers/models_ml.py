from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.model_ml import ModelTrainRequest, ModelTrainResponse, EvaluationResponse
from app.repositories.model_repository import ModelRepository
from app.repositories.dataset_repository import DatasetRepository
from app.services.model_service import ModelService

router = APIRouter(prefix="/models", tags=["Models"])

def get_model_service(db: Session = Depends(get_db)) -> ModelService:
    model_repo = ModelRepository(db)
    dataset_repo = DatasetRepository(db)
    return ModelService(model_repo, dataset_repo)

@router.post("/train", response_model=ModelTrainResponse, status_code=status.HTTP_201_CREATED)
def train_model(
    payload: ModelTrainRequest,
    service: ModelService = Depends(get_model_service)
):
    return service.train_naive_bayes(
        dataset_id=payload.dataset_id,
        test_size=payload.test_size
    )

@router.get("/{id}/evaluation", response_model=EvaluationResponse, status_code=status.HTTP_200_OK)
def evaluate_model(
    id: int,
    service: ModelService = Depends(get_model_service)
):
    return service.get_evaluation(model_id=id)