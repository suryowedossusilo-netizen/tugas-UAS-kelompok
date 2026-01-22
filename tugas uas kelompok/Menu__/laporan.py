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


def menu_laporan():
    data = load_barang()

    print("\n=== LAPORAN STOK BARANG ===")

    if not data:
        print("Belum ada data barang.")
        return

    total_nilai = 0

    print("-" * 60)
    print(f"{'ID':<10}{'Nama':<20}{'Harga':<10}{'Stok':<10}")
    print("-" * 60)

    for item in data:
        nilai = item["harga"] * item["stok"]
        total_nilai += nilai
        print(f"{item['id']:<10}{item['nama']:<20}{item['harga']:<10}{item['stok']:<10}")

    print("-" * 60)
    print(f"Total nilai stok: Rp {total_nilai}")
