# API Contract

## POST /api/auth/login
Request:
```json
{
  "username": "admin",
  "password": "password"
}
```

## POST /api/datasets
Upload dataset.

## GET /api/datasets
Mengambil daftar dataset.

## POST /api/models/train
Memulai training Naïve Bayes.

```json
{
  "dataset_id": 1,
  "test_size": 0.2
}
```

## GET /api/models/{id}/evaluation
Mengambil hasil evaluasi model.

## POST /api/predictions
Melakukan klasifikasi data baru.

```json
{
  "model_id": 1,
  "features": {}
}
```

Response:
```json
{
  "predicted_class": "class_a",
  "probabilities": {}
}
```
