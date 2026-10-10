from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class ModelTrainRequest(BaseModel):
    dataset_id: int
    test_size: float = Field(default=0.2, ge=0.05, le=0.5)

class ModelTrainResponse(BaseModel):
    id: int
    dataset_id: int
    name: str
    message: str = "Training berhasil"

    class Config:
        from_attributes = True

class EvaluationMetrics(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    confusion_matrix: Optional[list] = None

class EvaluationResponse(BaseModel):
    model_id: int
    metrics: Dict[str, Any]
    created_at: datetime