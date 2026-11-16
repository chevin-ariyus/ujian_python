def hapus_duplikat(data):
    """Menggunakan SET untuk melacak ID unik dan menghapus baris duplikat."""
    id_unik = set()
    data_bersih = []
    for item in data:
        if item['id'] not in id_unik:
            id_unik.add(item['id'])
            data_bersih.append(item)
    return data_bersih

def filter_kategori(data, kategori_cari):
    """Menggunakan LIST COMPREHENSION untuk menyaring data berdasarkan kategori."""
    return [item for item in data if item['kategori'].lower() == kategori_cari.lower()]

def rekap_stok_per_kategori(data):
    """Menggunakan DICTIONARY untuk mengelompokkan dan menjumlahkan stok."""
    rekap = {}
    for item in data:
        kategori = item['kategori']
        stok = int(item['stok']) 
        if kategori in rekap:
            rekap[kategori] += stok
        else:
            rekap[kategori] = stok
    return rekap