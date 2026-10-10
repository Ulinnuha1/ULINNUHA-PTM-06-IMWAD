from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class ModelML(Base):
    __tablename__ = "models_ml"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    model_path = Column(String, nullable=False)
    scaler_path = Column(String, nullable=True)
    test_size = Column(Float, default=0.2)
    metrics = Column(JSON, nullable=True)  # Menyimpan accuracy, precision, recall, f1-score, dll.
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    dataset = relationship("Dataset", back_populates="models")