# Software Requirements Specification (SRS)

## 1. Functional Requirements

### FR-01 Login
Sistem menyediakan autentikasi pengguna yang berwenang.

### FR-02 Dataset
Pengguna dapat mengunggah dataset untuk proses klasifikasi.

### FR-03 Validasi Dataset
Sistem memeriksa format file, kolom, data kosong, dan kelas target.

### FR-04 Preprocessing
Sistem melakukan pembersihan dan penyiapan data sesuai tipe atribut.

### FR-05 Training
Sistem membagi dataset menjadi data training dan testing kemudian melatih model Naïve Bayes.

### FR-06 Evaluasi
Sistem menghitung metrik evaluasi berdasarkan hasil data testing.

### FR-07 Prediksi
Pengguna dapat memasukkan data baru dan sistem memberikan kelas hasil prediksi.

### FR-08 Riwayat
Sistem menyimpan informasi proses klasifikasi dan hasil prediksi.

## 2. Business Rules
- Dataset harus memiliki atribut target.
- Data training harus memiliki label kelas.
- Data baru harus mengikuti struktur atribut model.
- Model hanya dapat digunakan setelah proses training berhasil.

## 3. Data Requirements
Entitas utama:
- users
- datasets
- dataset_rows
- models
- predictions
- evaluations

## 4. Acceptance Criteria
Sistem dianggap berhasil apabila dataset dapat diproses, model Naïve Bayes dapat dilatih, hasil evaluasi dapat ditampilkan, dan data baru dapat diklasifikasikan.
