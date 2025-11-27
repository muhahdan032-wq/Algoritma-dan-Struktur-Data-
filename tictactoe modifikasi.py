# Muhammad Ahdan
# D0425317
import tkinter as tk
from tkinter import messagebox

# Warna pemain
WARNA_X = "#ff4d4d"   # merah
WARNA_O = "#4d79ff"   # biru
WARNA_BG = "#f0f0f0"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg=WARNA_BG)
        
        self.current_player = "X"
        self.buttons = []
        self.board = [" " for _ in range(9)]

        self.label_info = tk.Label(
            root, text="Giliran Pemain: X",
            font=("Arial", 16, "bold"),
            bg=WARNA_BG
        )
        self.label_info.pack(pady=10)

        self.frame = tk.Frame(root, bg=WARNA_BG)
        self.frame.pack()

        self.buat_tombol()

        self.reset_button = tk.Button(
            root, text="Reset Game", font=("Arial", 14),
            command=self.reset_game
        )
        self.reset_button.pack(pady=10)

    def buat_tombol(self):
        for i in range(9):
            btn = tk.Button(
                self.frame, text="", font=("Arial", 30, "bold"),
                width=5, height=2,
                command=lambda index=i: self.klik(index)
            )
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def klik(self, index):
        if self.board[index] != " ":
            return

        self.board[index] = self.current_player

        if self.current_player == "X":
            self.buttons[index].config(text="X", fg=WARNA_X)
        else:
            self.buttons[index].config(text="O", fg=WARNA_O)

        if self.cek_pemenang():
            messagebox.showinfo("Selesai", f"Pemain {self.current_player} menang!")
            self.disable_all_buttons()
            return

        if self.cek_seri():
            messagebox.showinfo("Selesai", "Hasil: Seri!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.label_info.config(text=f"Giliran Pemain: {self.current_player}")

    def cek_pemenang(self):
        kombinasi_menang = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in kombinasi_menang:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                # Highlight pemenang
                self.buttons[a].config(bg="#ffff99")
                self.buttons[b].config(bg="#ffff99")
                self.buttons[c].config(bg="#ffff99")
                return True
        return False

    def cek_seri(self):
        return all(cell != " " for cell in self.board)

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.label_info.config(text="Giliran Pemain: X")

        self.board = [" " for _ in range(9)]
        for btn in self.buttons:
            btn.config(text="", bg="SystemButtonFace", state="normal")


# Menjalankan Game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
