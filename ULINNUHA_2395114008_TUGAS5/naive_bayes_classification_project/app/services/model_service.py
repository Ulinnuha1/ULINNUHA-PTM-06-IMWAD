class ModelService:
    def __init__(self, model_repo=None, dataset_repo=None):
        self.model_repo = model_repo
        self.dataset_repo = dataset_repo

    def train_naive_bayes(self, dataset_id: int, test_size: float = 0.2):
        pass

    def get_evaluation(self, model_id: int):
        pass