from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class DatasetBase(BaseModel):
    filename: str
    description: Optional[str] = None

class DatasetCreate(DatasetBase):
    file_path: str
    uploaded_by: Optional[int] = None

class DatasetResponse(DatasetBase):
    id: int
    file_path: str
    uploaded_by: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True