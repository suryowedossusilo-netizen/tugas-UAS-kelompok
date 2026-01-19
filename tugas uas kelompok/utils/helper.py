import os
from datetime import datetime

# Bersihkan layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Pause / tekan enter
def pause():
    input("\nTekan ENTER untuk melanjutkan...")


# Format rupiah
def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")


# Ambil tanggal sekarang
def tanggal_sekarang():
    return datetime.now().strftime("%Y-%m-%d")


# Ambil waktu sekarang
def waktu_sekarang():
    return datetime.now().strftime("%H:%M:%S")


# Cek apakah file ada
def cek_file(path):
    return os.path.exists(path)


# Buat file jika belum ada
def buat_file_jika_belum_ada(path, header=""):
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(header + "\n")
