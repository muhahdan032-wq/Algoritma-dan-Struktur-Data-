# Nama   : Muhammad Ahdan
# NIM    : D0425317
# Kelas  : B Sistem Informasi

# =====================================================
# 1) Struktur Sekuensial
# Eksekusi berjalan berurutan dari atas ke bawah,
# tanpa percabangan maupun pengulangan.
# =====================================================

print("Masukkan nama Anda:")
user = input()
print("Halo,", user)

# =====================================================
# 2) Struktur Seleksi (Percabangan)
# Digunakan untuk memilih aksi berdasarkan kondisi.
# Bentuk umum: if, if-else, if-elif-else
# =====================================================

skor = 75

if skor >= 70:
    print("Status: Lulus")
else:
    print("Status: Tidak Lulus")

# =====================================================
# 3) Struktur Perulangan (Looping)
# Menjalankan perintah secara berulang selama syarat terpenuhi.
# Dua jenis umum: for dan while
# =====================================================

for angka in range(1, 6):
    print(angka)

# =====================================================
# 4) Struktur Modular (Fungsi)
# Memecah program menjadi bagian kecil agar mudah dibaca & dirawat.
# =====================================================

def sambutan():
    print("Selamat datang di program Python")

sambutan()

# =====================================================
# 5) Struktur Data Pendukung
# Digunakan untuk menyimpan dan mengatur kumpulan data.
# Contoh: variabel, list, dictionary, tuple, dll.
# =====================================================

daftar_nilai = [80, 85, 90]
