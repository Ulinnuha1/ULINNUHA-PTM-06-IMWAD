from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import User, Dataset, ModelML  # register SQLAlchemy models
from app.routers import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Naive Bayes Classification API",
    version="1.0.0",
    description="REST API untuk aplikasi klasifikasi menggunakan algoritma Naive Bayes.",
)

app.include_router(api_router, prefix="/api")


@app.get("/", tags=["Health Check"])
def root():
    return {"status": "ok", "message": "API Naive Bayes Classification berjalan"}
