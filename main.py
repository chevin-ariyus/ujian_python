from inventaris_pkg import file_handler, data_manager

def main():
    file_input = 'data/data_input.csv'
    file_output = 'data/data_output.csv'
    
   
    data_inventaris = file_handler.baca_data(file_input)
    
    if not data_inventaris:
        return
        
  
    data_inventaris = data_manager.hapus_duplikat(data_inventaris)

    while True:
        print("\n=== APLIKASI INVENTARIS ===")
        print("1. Tampilkan Semua Barang (Tanpa Duplikat)")
        print("2. Filter Berdasarkan Kategori")
        print("3. Rekap Total Stok per Kategori")
        print("4. Simpan & Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            for item in data_inventaris:
                print(item)
                
        elif pilihan == '2':
            kategori = input("Masukkan nama kategori (contoh: Elektronik): ")
            hasil_filter = data_manager.filter_kategori(data_inventaris, kategori)
            if hasil_filter:
                for item in hasil_filter:
                    print(item)
            else:
                print("Kategori tidak ditemukan.")
                
        elif pilihan == '3':
            rekap = data_manager.rekap_stok_per_kategori(data_inventaris)
            for kat, total in rekap.items():
                print(f"Kategori: {kat} | Total Stok: {total}")
                
        elif pilihan == '4':
            file_handler.simpan_data(file_output, data_inventaris)
            print("Program selesai.")
            break
            
        else:
            print("Pilihan tidak valid. Harap masukkan angka 1-4.")

if __name__ == "__main__":
    main()