import csv

def baca_data(nama_file):
    """Membaca file CSV dan mengembalikannya sebagai list of dictionary."""
    data = []
    try:
        with open(nama_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for baris in reader:
                data.append(baris)
        return data
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan!")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def simpan_data(nama_file, data):
    """Menyimpan list of dictionary kembali ke file CSV."""
    if not data:
        return
    try:
        with open(nama_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Data berhasil disimpan ke", nama_file)
    except Exception as e:
        print("Gagal menyimpan data:", e)