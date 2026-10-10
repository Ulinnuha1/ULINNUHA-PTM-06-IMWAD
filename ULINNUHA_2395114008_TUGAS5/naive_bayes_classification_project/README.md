# Naive Bayes Classification Project

REST API berbasis FastAPI untuk pengelolaan dataset dan klasifikasi Naïve Bayes.

## Persyaratan
- Python 3.10 atau lebih baru
- Terminal berada di folder `naive_bayes_classification_project`

## Menjalankan di Windows (PowerShell / terminal VS Code)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn main:app --reload
```

Jika memakai Command Prompt (CMD), aktivasi dengan `.venv\Scripts\activate.bat`.
Jika perintah `py` tidak tersedia, gunakan `python` sebagai gantinya. Jika PowerShell menolak aktivasi, jalankan server dengan `.venv\Scripts\python.exe -m uvicorn main:app --reload`.

## Membuka API
- Health check: http://127.0.0.1:8000/
- Dokumentasi interaktif: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Catatan
Repository untuk dataset dan model telah ditambahkan agar impor aplikasi tidak gagal. Implementasi pelatihan model dan prediksi masih berupa kerangka pada service; endpoint tersebut perlu dilengkapi sebelum digunakan untuk klasifikasi sungguhan. Untuk penggunaan selain pengembangan lokal, ganti `SECRET_KEY` dan konfigurasi database melalui `.env`.
