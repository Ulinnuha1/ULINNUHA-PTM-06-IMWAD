from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.model_ml import ModelML


class ModelRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, model_id: int) -> Optional[ModelML]:
        return self.db.query(ModelML).filter(ModelML.id == model_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelML]:
        return self.db.query(ModelML).offset(skip).limit(limit).all()

    def create(self, values: dict) -> ModelML:
        model = ModelML(**values)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model

    def update(self, model_id: int, values: dict) -> Optional[ModelML]:
        model = self.get_by_id(model_id)
        if model is None:
            return None
        for key, value in values.items():
            setattr(model, key, value)
        self.db.commit()
        self.db.refresh(model)
        return model
