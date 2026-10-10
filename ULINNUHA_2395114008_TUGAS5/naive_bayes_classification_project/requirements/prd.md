# Product Requirements Document (PRD)

## 1. Ringkasan Produk
Aplikasi klasifikasi berbasis web untuk membantu pengguna mengolah dataset dan menerapkan algoritma Naïve Bayes secara terstruktur. Sistem menyediakan proses input data, preprocessing, training, testing, evaluasi, serta klasifikasi data baru.

## 2. Masalah
Proses klasifikasi dataset secara manual membutuhkan perhitungan probabilitas dan pengelolaan data yang cukup banyak. Pengguna membutuhkan aplikasi yang dapat membantu menjalankan proses klasifikasi secara konsisten dan menampilkan hasilnya secara mudah dipahami.

## 3. Tujuan Produk
- Mempermudah pengolahan dataset klasifikasi.
- Mengotomatisasi perhitungan Naïve Bayes.
- Menampilkan hasil klasifikasi.
- Menyediakan evaluasi model melalui confusion matrix, accuracy, precision, recall, dan F1-score jika data uji memungkinkan.

## 4. Target Pengguna
- Admin/pengelola dataset.
- Peneliti atau mahasiswa.
- Pengguna yang membutuhkan hasil klasifikasi dari data yang tersedia.

## 5. Fitur Utama
### Must Have
- Login sederhana untuk admin.
- Import dataset.
- Validasi dan preprocessing.
- Menentukan atribut dan kelas target.
- Pembagian data training/testing.
- Training model Naïve Bayes.
- Prediksi data baru.
- Hasil klasifikasi.
- Evaluasi model.

### Should Have
- Riwayat proses klasifikasi.
- Dashboard ringkasan hasil.
- Export hasil.

## 6. Non-Functional Requirements
- Antarmuka mudah digunakan.
- Validasi input.
- Waktu proses wajar untuk dataset aplikasi.
- Data tersimpan terstruktur.
- API menggunakan JSON.
