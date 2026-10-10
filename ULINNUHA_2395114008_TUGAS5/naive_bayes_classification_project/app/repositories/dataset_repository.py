from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.dataset import Dataset
from app.schemas.dataset import DatasetCreate


class DatasetRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, dataset_id: int) -> Optional[Dataset]:
        return self.db.query(Dataset).filter(Dataset.id == dataset_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Dataset]:
        return self.db.query(Dataset).offset(skip).limit(limit).all()

    def create(self, dataset_data: DatasetCreate) -> Dataset:
        dataset = Dataset(
            filename=dataset_data.filename,
            file_path=dataset_data.file_path,
            description=dataset_data.description,
            uploaded_by=dataset_data.uploaded_by,
        )
        self.db.add(dataset)
        self.db.commit()
        self.db.refresh(dataset)
        return dataset

    def delete(self, dataset_id: int) -> bool:
        dataset = self.get_by_id(dataset_id)
        if dataset is None:
            return False
        self.db.delete(dataset)
        self.db.commit()
        return True
