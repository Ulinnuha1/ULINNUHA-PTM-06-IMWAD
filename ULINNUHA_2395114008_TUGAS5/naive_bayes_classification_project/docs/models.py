from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass
class Dataset:
    id: int
    user_id: int
    name: str
    target_column: str
    created_at: datetime

@dataclass
class Model:
    id: int
    dataset_id: int
    algorithm: str = "Naive Bayes"
    status: str = "trained"

@dataclass
class Evaluation:
    model_id: int
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    confusion_matrix: Any

@dataclass
class Prediction:
    model_id: int
    predicted_class: str
    probabilities: dict
