from menu_.tambah_barang import menu_tambah_barang
from menu_.edit_barang import menu_edit_barang
from menu_.laporan import menu_laporan


def menu_utama():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Barang")
        print("2. Edit Barang")
        print("3. Laporan")
        print("4. Keluar")

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            menu_tambah_barang()
        elif pilih == "2":
            menu_edit_barang()
        elif pilih == "3":
            menu_laporan()
        elif pilih == "4":
            print("Keluar.")
            break
        else:
            print("Pilihan tidak valid.")

print =menu_utama()
