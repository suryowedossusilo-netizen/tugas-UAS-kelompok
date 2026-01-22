import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "barang.csv")


def load_barang():
    data = []
    if not os.path.exists(DATA_PATH):
        return data

    with open(DATA_PATH, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["harga"] = int(row["harga"])
            row["stok"] = int(row["stok"])
            data.append(row)
    return data


def save_barang(data):
    with open(DATA_PATH, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "nama", "harga", "stok"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


def menu_edit_barang():
    data = load_barang()

    print("\n=== EDIT BARANG ===")
    id_barang = input("Masukkan ID barang: ").strip()

    for item in data:
        if item["id"] == id_barang:
            print(f"Nama lama  : {item['nama']}")
            print(f"Harga lama : {item['harga']}")
            print(f"Stok lama  : {item['stok']}")

            nama_baru = input("Nama baru : ").strip()
            harga_baru = input("Harga baru : ").strip()
            stok_baru = input("Stok baru : ").strip()

            if nama_baru:
                item["nama"] = nama_baru

            if harga_baru:
                try:
                    harga_baru = int(harga_baru)
                    if harga_baru <= 0:
                        print("Harga harus > 0.")
                        return
                    item["harga"] = harga_baru
                except ValueError:
                    print("Harga harus angka.")
                    return

            if stok_baru:
                try:
                    stok_baru = int(stok_baru)
                    if stok_baru < 0:
                        print("Stok tidak boleh negatif.")
                        return
                    item["stok"] = stok_baru
                except ValueError:
                    print("Stok harus angka.")
                    return

            save_barang(data)
            print("Barang berhasil diperbarui.")
            return

    print("Barang tidak ditemukan.")
