# Nama   : Muhammad Ahdan
# NIM    : D0425317
# Kelas  : B Sistem Informasi

# =====================================================
# Konsep Union dalam Python
# =====================================================
# Dalam Python, istilah "union" biasanya merujuk pada dua hal:
# 1) Operasi penggabungan pada himpunan (set)
# 2) Union sebagai anotasi tipe (type hint) yang memperbolehkan
#    satu variabel memiliki lebih dari satu tipe data.

# -----------------------------------------------------
# 1) Union pada Himpunan (Set)
# Menggabungkan dua set dan menghapus elemen yang duplikat.
# -----------------------------------------------------

set_A = {1, 2, 3}
set_B = {3, 4, 5}

hasil_union = set_A.union(set_B)
print(hasil_union)

# -----------------------------------------------------
# 2) Union pada Tipe Data (Type Hint)
# Menandakan bahwa variabel bisa menyimpan lebih dari satu tipe.
# -----------------------------------------------------

from typing import Union

angka: Union[int, float]
angka = 10
angka = 10.5   # variabel ini sah-sah saja berubah ke tipe float

# Contoh fungsi menggunakan Union sebagai tipe parameter
from typing import Union

def tampilkan(value: Union[int, str]):
    print(value)

tampilkan(10)
tampilkan("Halo")
