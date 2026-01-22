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
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    with open(DATA_PATH, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "nama", "harga", "stok"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


def menu_tambah_barang():
    data = load_barang()

    print("\n=== TAMBAH BARANG ===")
    id_barang = input("ID Barang: ").strip()
    nama = input("Nama Barang: ").strip()

    if not id_barang or not nama:
        print("ID dan nama tidak boleh kosong.")
        return

    for item in data:
        if item["id"] == id_barang:
            print("ID barang sudah ada.")
            return

    try:
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
    except ValueError:
        print("Harga dan stok harus angka.")
        return

    if harga <= 0 or stok < 0:
        print("Harga harus > 0 dan stok tidak boleh negatif.")
        return

    data.append({
        "id": id_barang,
        "nama": nama,
        "harga": harga,
        "stok": stok
    })

    save_barang(data)
    print("Barang berhasil ditambahkan.")
