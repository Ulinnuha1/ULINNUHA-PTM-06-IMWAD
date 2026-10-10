# Low Level Design (LLD)

## 1. Modul Dataset
Tanggung jawab:
- upload dataset
- validasi format
- membaca baris data
- menentukan target class
- menyimpan dataset

## 2. Modul Preprocessing
Tahapan:
1. pemeriksaan nilai kosong
2. pembersihan data
3. encoding atribut kategorikal jika diperlukan
4. penentuan fitur dan target
5. pembagian data training dan testing

## 3. Modul Naïve Bayes
Input:
- data training
- label kelas
- data testing atau data baru

Output:
- kelas prediksi
- probabilitas prediksi

Rumus dasar:

P(C|X) = P(X|C) × P(C) / P(X)

Untuk beberapa fitur:

P(C|X) ∝ P(C) × P(x1|C) × P(x2|C) × ... × P(xn|C)

## 4. Modul Evaluation
Menghasilkan:
- confusion matrix
- accuracy
- precision
- recall
- F1-score

## 5. Modul Prediction
Pengguna mengisi fitur data baru → backend melakukan preprocessing → model Naïve Bayes menghasilkan probabilitas → sistem menampilkan kelas prediksi.
