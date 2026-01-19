# ============================
# FORMAT TAMPILAN KASIR
# ============================

def garis(panjang=40):
    return "-" * panjang


def judul(text):
    print(garis())
    print(text.center(40))
    print(garis())


def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")


def header_tabel():
    print(garis())
    print(f"{'Kode':<8} {'Nama':<15} {'Harga':<10} {'Stok':<5}")
    print(garis())


def baris_barang(kode, nama, harga, stok):
    print(f"{kode:<8} {nama:<15} {rupiah(harga):<10} {stok:<5}")


def header_transaksi():
    print(garis())
    print(f"{'Nama':<15} {'Qty':<5} {'Harga':<10} {'Total':<10}")
    print(garis())


def baris_transaksi(nama, qty, harga):
    total = qty * harga
    print(f"{nama:<15} {qty:<5} {rupiah(harga):<10} {rupiah(total):<10}")
