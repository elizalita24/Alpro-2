import time

def total_belanjaan():
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    
    barang = []  # List untuk menyimpan (nama, harga)
    
    for i in range(jumlah_barang):
        nama = input(f"Masukkan nama barang ke-{i+1}: ")
        harga = int(input(f"Masukkan harga {nama}: "))
        barang.append((nama, harga))  # Simpan sebagai tuple (nama, harga)

    start_time = time.perf_counter()  # Mulai hitung waktu lebih presisi

    total = sum(harga for _, harga in barang)  # Hitung total harga
    barang_termahal = max(barang, key=lambda x: x[1])  # Cari barang dengan harga tertinggi
    barang_termurah = min(barang, key=lambda x: x[1])  # Cari barang dengan harga terendah

    end_time = time.perf_counter()  # Selesai hitung waktu

    print("\n=== Rincian Belanja ===")
    for nama, harga in barang:
        print(f"{nama}: Rp{harga:,}")

    print(f"\nTotal belanja: Rp{total:,}")
    print(f"Barang termahal: {barang_termahal[0]} - Rp{barang_termahal[1]:,}")
    print(f"Barang termurah: {barang_termurah[0]} - Rp{barang_termurah[1]:,}")
    print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")  # Lebih presisi

# Jalankan program
total_belanjaan()
