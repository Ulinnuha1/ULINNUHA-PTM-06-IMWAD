from sqlalchemy.orm import Session

class DatasetService:
    def __init__(self, repo=None):
        self.repo = repo

    def list_datasets(self, skip: int = 0, limit: int = 100):
        pass

    def upload_dataset(self, file, description: str = None):
        pass