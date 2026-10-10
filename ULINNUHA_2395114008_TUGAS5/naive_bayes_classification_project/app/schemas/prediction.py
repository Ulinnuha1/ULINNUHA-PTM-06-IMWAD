from typing import Dict, Any, List
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    model_id: int
    features: Dict[str, Any]

class PredictionResponse(BaseModel):
    model_id: int
    predicted_class: Any
    probabilities: Dict[str, float]