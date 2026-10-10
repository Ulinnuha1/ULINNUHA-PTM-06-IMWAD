from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, Form, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.dataset import DatasetResponse
from app.repositories.dataset_repository import DatasetRepository
from app.services.dataset_service import DatasetService

router = APIRouter(prefix="/datasets", tags=["Datasets"])

def get_dataset_service(db: Session = Depends(get_db)) -> DatasetService:
    repo = DatasetRepository(db)
    return DatasetService(repo)

@router.get("", response_model=List[DatasetResponse], status_code=status.HTTP_200_OK)
def get_datasets(
    skip: int = 0,
    limit: int = 100,
    service: DatasetService = Depends(get_dataset_service)
):
    return service.list_datasets(skip=skip, limit=limit)

@router.post("", response_model=DatasetResponse, status_code=status.HTTP_201_CREATED)
def upload_dataset(
    file: UploadFile = File(...),
    description: str = Form(None),
    service: DatasetService = Depends(get_dataset_service)
):
    return service.upload_dataset(file=file, description=description)