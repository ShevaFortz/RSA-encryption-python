# 🔐 Implementasi Algoritma RSA Menggunakan Python

**Nama**  : Muhammad Reyhan Sheva RizQulah  
**NIM**   : 25051204261  
**Kelas** : TIH  

📎 Repository GitHub:  
https://github.com/ShevaFortz/RSA-encryption-python.git

LInk demo : https://drive.google.com/file/d/1XgHwvrtl8NJiN4lN2gQHTD5aGxB-T7B_/view?usp=drive_link

## 📌 Deskripsi Project

Project ini merupakan implementasi algoritma RSA (Rivest–Shamir–Adleman) menggunakan Python tanpa library enkripsi instan.

Semua proses seperti pencarian GCD, invers modulo, pembangkitan kunci, enkripsi, hingga dekripsi dibuat secara manual untuk memahami konsep matematika di balik kriptografi asimetris.

RSA menggunakan dua kunci:
- 🔓 **Public Key** → digunakan untuk enkripsi
- 🔐 **Private Key** → digunakan untuk dekripsi

---

## ⚙️ Konsep yang Digunakan

- Bilangan Prima
- Greatest Common Divisor (GCD)
- Extended Euclidean Algorithm
- Invers Modulo
- Aritmatika Modular
- Konversi Karakter ke ASCII

---

## 🔑 Tahap Pembangkitan Kunci

1. Memilih dua bilangan prima (p dan q)
2. Menghitung n = p × q
3. Menghitung φ(n) = (p-1)(q-1)
4. Memilih nilai e yang relatif prima terhadap φ(n)
5. Menghitung nilai d sebagai invers modulo dari e terhadap φ(n)

Public Key  : (e, n)  
Private Key : (d, n)

---

## 🔒 Proses Enkripsi

Setiap karakter pada pesan:
1. Diubah menjadi nilai ASCII menggunakan `ord()`
2. Diproses dengan rumus:
   C = M^e mod n
Hasilnya berupa deretan angka ciphertext.

---

## 🔓 Proses Dekripsi

Setiap angka ciphertext:
1. Diproses dengan rumus:
   M = C^d mod n
2. Hasil dikonversi kembali menjadi karakter menggunakan `chr()`
Jika kunci benar, hasil dekripsi akan sama dengan pesan awal.

---

## 🧪 Contoh Output Program

Plaintext : aku reyhan  
Ciphertext : [113, 6, 145, 43, 130, 118, 110, 59, 113, 121]  
Hasil Dekripsi : aku reyhan  

---

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Clone repository:
   ```bash
   git clone https://github.com/ShevaFortz/RSA-encryption-python.git
   ```
3. Masuk ke folder project
4. Jalankan file:
   ```bash
   python rsa.py
   ```
5. Masukkan pesan yang ingin dienkripsi
6. Program akan menampilkan proses enkripsi dan dekripsi di terminal

---

## 🎯 Tujuan Project
Project ini dibuat untuk memahami secara langsung bagaimana algoritma RSA bekerja dari sisi matematis maupun implementasi kode, tanpa bergantung pada library enkripsi bawaan.

---

⭐ Terima kasih telah melihat project ini.