# Nama  : Muhammad Ahdan
# NIM   : D0425317
# Kelas : B Sistem Informasi

# =====================================================
# 1. Tipe Data Character (Python menggunakan str)
# =====================================================
print("=== 1. STRING (str) ===")

huruf = "Z"
nama_bahasa = "Python"

# Operasi string
ambil_karakter = nama_bahasa[-2]        # mengambil karakter kedua dari belakang
jumlah_huruf = len(nama_bahasa)

print("Huruf:", huruf, "| Jenis:", type(huruf))
print("Karakter kedua dari belakang:", ambil_karakter)
print("Jumlah karakter pada kata 'Python':", jumlah_huruf)

print("=" * 40)

# =====================================================
# 2. Tipe Data Integer (int)
# =====================================================
print("=== 2. INTEGER (int) ===")

angka1 = 15
angka2 = -75
angkapanjang = 12345678901234567890

# Operasi integer
hasil_kali = angka1 * 3
hasil_mod = 17 % 4         # sisa hasil bagi

print("Angka Positif:", angka1, "| Tipe:", type(angka1))
print("Hasil Perkalian 15 * 3 =", hasil_kali)
print("Sisa pembagian 17 % 4 =", hasil_mod)

print("=" * 40)

# =====================================================
# 3. Tipe Data Float (float)
# =====================================================
print("=== 3. FLOAT (float) ===")

nilai_pi = 3.14159
nilai_notasi = 7.2e4        # 72000.0

# Operasi float
hasil_tambah = nilai_pi + 1.5
hasil_bagi = 20 / 6

print("Nilai PI:", nilai_pi, "| Tipe:", type(nilai_pi))
print("Nilai Notasi Ilmiah:", nilai_notasi)
print("PI + 1.5 =", hasil_tambah)
print("20 / 6 =", hasil_bagi)

print("=" * 40)
