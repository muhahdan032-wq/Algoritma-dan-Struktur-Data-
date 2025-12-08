# Nama   : Muhammad Ahdan
# NIM    : D0425317
# Kelas  : B Sistem Informasi

# =====================================================
# PERANCANGAN ARRAY, STRUKTUR & UNION
# =====================================================

# -----------------------------------------------------
# 1.) Algoritma Stack
# -----------------------------------------------------
# Stack merupakan struktur data dengan prinsip LIFO:
# elemen terakhir yang ditambahkan akan keluar lebih dulu.
# Operasi yang umum dipakai:
# - push   (menambah data ke atas stack)
# - pop    (mengambil/menghapus data paling atas)
# - peek   (melihat elemen teratas)
# - isEmpty (cek apakah stack kosong)
#
# Contoh:
# Data masuk  : 10 -> 20 -> 30
# Data keluar : 30 -> 20 -> 10

# -----------------------------------------------------
# 2.) Algoritma Searching
# -----------------------------------------------------
# Searching bertujuan menemukan posisi atau keberadaan data tertentu.
# Misal: mencari nilai 7 di dalam list [2, 5, 7, 9, 12].

# -----------------------------------------------------
# 3.) Algoritma Pengurutan Dasar
#    (Bubble Sort, Selection Sort, Insertion Sort)
# -----------------------------------------------------

# ============= BUBBLE SORT =============
nums = [5, 3, 8, 4, 2]
n = len(nums)

for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Bubble Sort:", nums)

# ============= SELECTION SORT =============
nums = [5, 3, 8, 4, 2]
n = len(nums)

for i in range(n):
    pos_min = i
    for j in range(i + 1, n):
        if nums[j] < nums[pos_min]:
            pos_min = j
    nums[i], nums[pos_min] = nums[pos_min], nums[i]

print("Selection Sort:", nums)

# ============= INSERTION SORT =============
nums = [5, 3, 8, 4, 2]
n = len(nums)

for i in range(1, n):
    kunci = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > kunci:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = kunci

print("Insertion Sort:", nums)

# -----------------------------------------------------
# 4.) Pengurutan Tingkat Lanjut
#     (Shell Sort, Merge Sort, Quick Sort)
# -----------------------------------------------------

# ============= SHELL SORT =============
angka = [8, 3, 7, 4, 9, 2]
n = len(angka)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        simpan = angka[i]
        j = i
        while j >= gap and angka[j - gap] > simpan:
            angka[j] = angka[j - gap]
            j -= gap
        angka[j] = simpan
    gap //= 2

print("Shell Sort:", angka)

# ============= MERGE SORT =============
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        kiri = lst[:mid]
        kanan = lst[mid:]

        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                lst[k] = kiri[i]
                i += 1
            else:
                lst[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            lst[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            lst[k] = kanan[j]
            j += 1
            k += 1

sample = [8, 3, 7, 4, 9, 2]
merge_sort(sample)
print("Merge Sort:", sample)

# ============= QUICK SORT =============
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    kiri = [x for x in arr if x < pivot]
    tengah = [x for x in arr if x == pivot]
    kanan = [x for x in arr if x > pivot]

    return quick_sort(kiri) + tengah + quick_sort(kanan)

hasil = quick_sort([8, 3, 7, 4, 9, 2])
print("Quick Sort:", hasil)

# -----------------------------------------------------
# Tambahan: Pengertian Pseudocode
# -----------------------------------------------------
# Pseudocode adalah cara menjelaskan algoritma
# menggunakan bahasa yang mudah dipahami manusia,
# mirip kode program tetapi tidak bisa dieksekusi langsung.
