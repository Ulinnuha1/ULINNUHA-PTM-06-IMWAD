# Use Cases

## UC-01 Login
**Aktor:** Admin  
**Tujuan:** Masuk ke aplikasi.

Alur:
1. Admin membuka halaman login.
2. Admin mengisi username dan password.
3. Sistem memvalidasi.
4. Sistem menampilkan dashboard.

## UC-02 Upload Dataset
**Aktor:** Admin  
**Tujuan:** Menambahkan dataset.

Alur:
1. Admin memilih file.
2. Sistem memvalidasi file.
3. Sistem menyimpan dataset.
4. Dataset muncul pada daftar dataset.

## UC-03 Training Model
**Aktor:** Admin  
**Tujuan:** Membuat model Naïve Bayes.

Alur:
1. Admin memilih dataset.
2. Admin menentukan pembagian data.
3. Sistem melakukan preprocessing.
4. Sistem melakukan training.
5. Sistem menyimpan model dan hasil evaluasi.

## UC-04 Prediksi
**Aktor:** Admin  
**Tujuan:** Mengklasifikasikan data baru.

Alur:
1. Admin memilih model.
2. Admin mengisi atribut data.
3. Sistem memproses input.
4. Sistem menjalankan Naïve Bayes.
5. Sistem menampilkan kelas dan probabilitas.
