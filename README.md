# Aplikasi Cek & Rekap Inventaris (CLI)

Program berbasis Command Line (CLI) menggunakan Python untuk mengolah data inventaris barang dari file CSV—mulai dari membersihkan data ganda, filter kategori, hingga rekap total stok.

## Struktur Folder
```text
ujian_python_inventaris/
├── data/
│   ├── data_input.csv       # Data mentah awal
│   └── data_output.csv      # Hasil data bersih setelah diproses
├── inventaris_pkg/          # Package buatan sendiri
│   ├── __init__.py
│   ├── data_manager.py      # Olah data (hapus duplikat, filter, rekap stok)
│   └── file_handler.py      # Baca & simpan file CSV[cite: 1, 2]
├── main.py                  # File utama untuk menjalankan menu CLI
└── README.md