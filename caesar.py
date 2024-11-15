import tkinter as tk
from tkinter import messagebox

# Fungsi untuk enkripsi Caesar Cipher
def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk dekripsi Caesar Cipher
def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Fungsi yang dijalankan ketika tombol Enkripsi ditekan
def proses_enkripsi():
    try:
        shift = int(entry_shift_enkripsi.get())
        plaintext = entry_plaintext_enkripsi.get("1.0", tk.END).strip()
        if plaintext:
            result = caesar_cipher_encrypt(plaintext, shift)
            entry_hasil_enkripsi.delete("1.0", tk.END)
            entry_hasil_enkripsi.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Masukkan plaintext untuk enkripsi")
    except ValueError:
        messagebox.showerror("Error", "Kunci harus berupa angka")

# Fungsi yang dijalankan ketika tombol Dekripsi ditekan
def proses_dekripsi():
    try:
        shift = int(entry_shift_dekripsi.get())
        ciphertext = entry_plaintext_dekripsi.get("1.0", tk.END).strip()
        if ciphertext:
            result = caesar_cipher_decrypt(ciphertext, shift)
            entry_hasil_dekripsi.delete("1.0", tk.END)
            entry_hasil_dekripsi.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Masukkan ciphertext untuk dekripsi")
    except ValueError:
        messagebox.showerror("Error", "Kunci harus berupa angka")

# Fungsi untuk menghapus teks di semua entri
def hapus():
    entry_plaintext_enkripsi.delete("1.0", tk.END)
    entry_hasil_enkripsi.delete("1.0", tk.END)
    entry_shift_enkripsi.delete(0, tk.END)
    entry_plaintext_dekripsi.delete("1.0", tk.END)
    entry_hasil_dekripsi.delete("1.0", tk.END)
    entry_shift_dekripsi.delete(0, tk.END)

# Inisialisasi window Tkinter
root = tk.Tk()
root.title("Aplikasi Enkripsi dan Dekripsi Caesar Cipher")
root.geometry("900x600")  # Ukuran window yang lebih besar
root.configure(bg="#f4c2c2")  # Tema warna keseluruhan pink lembut

# Label judul utama
tk.Label(root, text="CAESAR", font=("Arial", 26, "bold"), bg="#f4c2c2", fg="#ffffff").pack(pady=15)

# Frame utama untuk membagi enkripsi dan dekripsi
frame_main = tk.Frame(root, bg="#f4c2c2")
frame_main.pack(fill="both", expand=True, padx=20, pady=20)

# ================== Dekripsi ==================
frame_dekripsi = tk.LabelFrame(frame_main, text="Dekripsi", font=("Arial", 18, "bold"), bg="#ffffff", fg="#333333", padx=10, pady=10)
frame_dekripsi.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

tk.Label(frame_dekripsi, text="Masukkan Ciphertext", bg="#ffffff", fg="#333333", font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=5)
entry_plaintext_dekripsi = tk.Text(frame_dekripsi, height=5, width=30, font=("Arial", 12), relief=tk.SOLID, bd=1)
entry_plaintext_dekripsi.grid(row=1, column=0, pady=5)

tk.Label(frame_dekripsi, text="Pergeseran Kunci (Shift)", bg="#ffffff", fg="#333333", font=("Arial", 14)).grid(row=2, column=0, sticky="w", pady=5)
entry_shift_dekripsi = tk.Entry(frame_dekripsi, width=10, font=("Arial", 12), relief=tk.SOLID, bd=1)
entry_shift_dekripsi.grid(row=3, column=0, sticky="e", pady=5)

tk.Label(frame_dekripsi, text="Hasil Dekripsi:", bg="#ffffff", fg="#333333", font=("Arial", 14)).grid(row=4, column=0, sticky="w", pady=5)
entry_hasil_dekripsi = tk.Text(frame_dekripsi, height=5, width=30, font=("Arial", 12), relief=tk.SOLID, bd=1)
entry_hasil_dekripsi.grid(row=5, column=0, pady=5)

# Tombol Dekripsi diposisikan di tengah
button_dekripsi = tk.Button(frame_dekripsi, text="Dekripsi", command=proses_dekripsi, font=("Arial", 12, "bold"), width=20, bg="#f08080")
button_dekripsi.grid(row=6, column=0, pady=10)

# ================== Enkripsi ==================
frame_enkripsi = tk.LabelFrame(frame_main, text="Enkripsi", font=("Arial", 18, "bold"), bg="#ffffff", fg="#333333", padx=10, pady=10)
frame_enkripsi.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

tk.Label(frame_enkripsi, text="Masukkan Plaintext", bg="#ffffff", fg="#333333", font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=5)
entry_plaintext_enkripsi = tk.Text(frame_enkripsi, height=5, width=30, font=("Arial", 12), relief=tk.SOLID, bd=1)
entry_plaintext_enkripsi.grid(row=1, column=0, pady=5)

tk.Label(frame_enkripsi, text="Pergeseran Kunci (Shift)", bg="#ffffff", fg="#333333", font=("Arial", 14)).grid(row=2, column=0, sticky="w", pady=5)
entry_shift_enkripsi = tk.Entry(frame_enkripsi, width=10, font=("Arial", 12), relief=tk.SOLID, bd=1)
entry_shift_enkripsi.grid(row=3, column=0, sticky="e", pady=5)

tk.Label(frame_enkripsi, text="Hasil Enkripsi:", bg="#ffffff", fg="#333333", font=("Arial", 14)).grid(row=4, column=0, sticky="w", pady=5)
entry_hasil_enkripsi = tk.Text(frame_enkripsi, height=5, width=30, font=("Arial", 12), relief=tk.SOLID, bd=1)
entry_hasil_enkripsi.grid(row=5, column=0, pady=5)

# Tombol Enkripsi diposisikan di tengah
button_enkripsi = tk.Button(frame_enkripsi, text="Enkripsi", command=proses_enkripsi, font=("Arial", 12, "bold"), width=20, bg="#f08080")
button_enkripsi.grid(row=6, column=0, pady=10)

# Tombol Hapus dan Keluar di bagian bawah
frame_buttons = tk.Frame(root, bg="#f4c2c2")
frame_buttons.pack(pady=20)

tk.Button(frame_buttons, text="Hapus", command=hapus, font=("Arial", 12, "bold"), width=12, height=1, bg="#ffb6c1").grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Keluar", command=root.quit, font=("Arial", 12, "bold"), width=12, height=1, bg="#ff6347").grid(row=0, column=1, padx=10)

# Mengatur agar kedua frame enkripsi dan dekripsi berada di tengah dengan ukuran yang sama
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=1)

root.mainloop()
