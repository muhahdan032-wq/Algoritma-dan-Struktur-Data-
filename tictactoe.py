# Muhammad Ahdan
# D0425317
# tic_tac_toe.py
# Game Tic-Tac-Toe (XO) untuk 2 pemain lokal di terminal
# Ditulis dengan komentar bahasa Indonesia agar mudah dimengerti.

def buat_board_kosong():
    """
    Membuat board kosong sebagai list dengan 9 elemen.
    Indeks 0..8 merepresentasikan posisi 1..9 pada papan.
    """
    return [" " for _ in range(9)]


def tampilkan_board(board):
    """
    Menampilkan board ke terminal dengan format 3x3.
    Board adalah list panjang 9.
    """
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def validasi_input_posisi(teks_input, board):
    """
    Memeriksa apakah input posisi valid:
      - Bisa dikonversi ke integer antara 1 sampai 9
      - Posisi tersebut kosong di board
    Mengembalikan (True, posisi_index) jika valid, atau (False, pesan_error) jika tidak.
    """
    teks_input = teks_input.strip()
    if not teks_input.isdigit():
        return False, "Masukan harus berupa angka 1-9."
    pos = int(teks_input)
    if pos < 1 or pos > 9:
        return False, "Pilihan harus antara 1 sampai 9."
    idx = pos - 1
    if board[idx] != " ":
        return False, "Posisi sudah diisi. Pilih posisi lain."
    return True, idx


def cek_pemenang(board):
    """
    Mengecek apakah ada pemenang.
    Mengembalikan "X" atau "O" jika ada pemenang, atau None jika belum ada.
    Kombinasi pemenang: 3 baris, 3 kolom, 2 diagonal.
    """
    menang_kombinasi = [
        (0,1,2), (3,4,5), (6,7,8),  # baris
        (0,3,6), (1,4,7), (2,5,8),  # kolom
        (0,4,8), (2,4,6)            # diagonal
    ]
    for a, b, c in menang_kombinasi:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def cek_seri(board):
    """
    Mengecek apakah board penuh (seri) dan tidak ada pemenang.
    """
    return all(cell != " " for cell in board)


def giliran_pemain(current_player, board):
    """
    Menangani masukan giliran pemain.
    Mengambil input dari pengguna sampai mendapat posisi yang valid.
    Mengubah board sesuai pilihan.
    """
    while True:
        pengguna = input(f"Pemain {current_player}, masukkan posisi (1-9): ")
        valid, hasil = validasi_input_posisi(pengguna, board)
        if valid:
            board[hasil] = current_player
            break
        else:
            print("Input tidak valid:", hasil)


def main():
    """
    Fungsi utama untuk menjalankan game.
    Mengatur giliran pemain, menampilkan board, mengecek pemenang/seri, dan mengulang.
    """
    print("Selamat datang di Tic-Tac-Toe!")
    print("Posisi papan diberi nomor seperti berikut:")
    contoh_board = [str(i) for i in range(1, 10)]
    tampilkan_board(contoh_board)

    board = buat_board_kosong()
    current_player = "X"  # X mulai duluan secara konvensional

    while True:
        tampilkan_board(board)
        giliran_pemain(current_player, board)

        # Cek pemenang setelah setiap langkah
        pemenang = cek_pemenang(board)
        if pemenang:
            tampilkan_board(board)
            print(f"🎉 Pemain {pemenang} menang! Selamat!")
            break

        # Cek seri (board penuh)
        if cek_seri(board):
            tampilkan_board(board)
            print("Hasil: Seri. Tidak ada pemenang.")
            break

        # Ganti giliran
        current_player = "O" if current_player == "X" else "X"

    print("Terima kasih sudah bermain!")

if __name__ == "__main__":
    main()
