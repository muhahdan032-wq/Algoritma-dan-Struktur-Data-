# Nama   : Muhammad Ahdan
# NIM    : D0425317
# Kelas  : B Sistem Informasi

# ---------------------------------------------------------
# Array 1 Dimensi: Kumpulan nilai beberapa siswa
# ---------------------------------------------------------
daftar_nilai = [90, 75, 88, 92, 70]

# Mengambil elemen indeks ke-2 (nilai ketiga)
print(f"Nilai pada indeks 2: {daftar_nilai[2]}")

# ---------------------------------------------------------
# Array 2 Dimensi: Nilai siswa untuk dua mata pelajaran
# Bentuk: [ [MTK, IPA], ... ]
# ---------------------------------------------------------
nilai_matriks = [
    [80, 95],   # Data siswa pertama
    [75, 88],   # Data siswa kedua
    [92, 79]    # Data siswa ketiga
]

# Mengambil nilai IPA siswa ke-2 (baris 1, kolom 1)
nilai_ipa_s2 = nilai_matriks[1][1]
print(f"IPA Siswa 2: {nilai_ipa_s2}")

# ---------------------------------------------------------
# Array 3 Dimensi: Data kelas A dan B
# Format: Halaman -> Siswa -> [MTK, IPA]
# ---------------------------------------------------------
nilai_3d = [
    # Data kelas A
    [
        [90, 85],   # Siswa 1
        [70, 75]    # Siswa 2
    ],
    # Data kelas B
    [
        [95, 88],   # Siswa 3
        [80, 92]    # Siswa 4
    ]
]

# Mengambil nilai MTK siswa 3 yang berada pada kelas B (halaman 1)
nilai_mtk_s3_b = nilai_3d[1][0][0]
print(f"MTK Siswa 3 (Kelas B): {nilai_mtk_s3_b}")
