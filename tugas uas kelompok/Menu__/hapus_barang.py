def hapus_barang(keranjang_nama, keranjang_harga, keranjang_jumlah):
    """
    Fungsi untuk menghapus barang dari keranjang belanja
    """
    
    if len(keranjang_nama) == 0:
        print("\n❌ Keranjang belanja masih kosong!")
        return keranjang_nama, keranjang_harga, keranjang_jumlah
    
 
    print("\n" + "="*60)
    print("DAFTAR BARANG DI KERANJANG")
    print("="*60)
    print(f"{'No.':<5} {'Nama Barang':<20} {'Harga':<15} {'Jumlah':<10}")
    print("-"*60)
    
    for i in range(len(keranjang_nama)):
        print(f"{i+1:<5} {keranjang_nama[i]:<20} "
              f"Rp {keranjang_harga[i]:<12,.0f} "
              f"{keranjang_jumlah[i]:<10}")
    
    print("="*60)
    
    while True:
        try:
            pilihan = input("\nMasukkan nomor barang yang akan dihapus (0 untuk batal): ").strip()
        
            if pilihan == "0":
                print("Penghapusan dibatalkan.")
                return keranjang_nama, keranjang_harga, keranjang_jumlah
            
       
            nomor = int(pilihan)
      
            if 1 <= nomor <= len(keranjang_nama):
                
                nama_barang = keranjang_nama[nomor-1]
                konfirmasi = input(f"Apakah yakin menghapus '{nama_barang}'? (y/n): ").lower()
                
                if konfirmasi == 'y':
                  
                    barang_dihapus = keranjang_nama.pop(nomor-1)
                    harga_dihapus = keranjang_harga.pop(nomor-1)
                    jumlah_dihapus = keranjang_jumlah.pop(nomor-1)
                    
                    print(f"\n✅ Barang '{barang_dihapus}' berhasil dihapus!")
                    print(f"   - Harga: Rp {harga_dihapus:,.0f}")
                    print(f"   - Jumlah: {jumlah_dihapus}")
                    
                   
                    if len(keranjang_nama) > 0:
                        print(f"\nSisa barang di keranjang: {len(keranjang_nama)} item")
                    else:
                        print("\nKeranjang sekarang kosong.")
                    
                    break
                else:
                    print("Penghapusan dibatalkan.")
                    break
            else:
                print(f"❌ Nomor tidak valid! Masukkan angka 1 sampai {len(keranjang_nama)}")
                
        except ValueError:
            print("❌ Masukkan angka yang valid!")
        except KeyboardInterrupt:
            print("\n\nOperasi dibatalkan oleh pengguna.")
            return keranjang_nama, keranjang_harga, keranjang_jumlah
    
    return keranjang_nama, keranjang_harga, keranjang_jumlah
