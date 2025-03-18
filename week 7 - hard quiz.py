import time

# Data Destinasi & Biaya
destinasi = {
    "Jatimpark 1 + Museum Angkut": 150000,
    "Batu Night Spectacular + wahana": 125000,
    "Eco Green Park": 50000,
    "Batu Love Garden": 50000
}

hidden_gem = {
    "Taman Dolan": 20000,
    "Wisata Alam Brakseng": 15000,
    "Coban Rondo": 40000,
}

hotel = {
    "Golden Tulip Holland Resort Batu": 2100000
}

transportasi = {
    "Sewa Mobil (3 hari)": 1650000,
    "Bensin": 650000,
}

jajanan = 650000  # Total jajanan 3 hari
budget_total = 5500000  # Maksimal budget

# Meminta input biaya tak terduga
biaya_tak_terduga = int(input("Masukkan biaya tak terduga (Rp): "))
budget_total -= biaya_tak_terduga  # Sesuaikan budget setelah pengeluaran tak terduga

# Variabel untuk menyimpan hasil terbaik
best_plan = None
best_cost = float('inf')

# Backtracking untuk mencari kombinasi terbaik
def cari_liburan(path_destinasi=[], path_hg=[], idx_destinasi=0, idx_hg=0):
    global best_plan, best_cost

    if len(path_destinasi) == 4 and len(path_hg) > 0:
        total_transport = sum(transportasi.values())
        total_biaya = (
            sum(destinasi[d] for d in path_destinasi) +
            sum(hidden_gem[hg] for hg in path_hg) +
            total_transport +
            jajanan +
            hotel["Golden Tulip Holland Resort Batu"]
        )

        if abs(total_biaya - budget_total) < abs(best_cost - budget_total):
            best_plan = (path_destinasi, path_hg, total_biaya)
            best_cost = total_biaya

        return

    for i in range(idx_destinasi, len(destinasi.keys())):
        if len(path_destinasi) < 4:
            cari_liburan(path_destinasi + [list(destinasi.keys())[i]], path_hg, i + 1, idx_hg)
    
    for j in range(idx_hg, len(hidden_gem.keys())):
        if len(path_hg) < len(hidden_gem):
            cari_liburan(path_destinasi, path_hg + [list(hidden_gem.keys())[j]], idx_destinasi, j + 1)

# Menjalankan Backtracking
start_time = time.time()
cari_liburan()
execution_time = time.time() - start_time

# Jika total biaya masih melebihi budget, hapus destinasi atau hidden gem
if best_plan:
    path_destinasi, path_hg, total_biaya = best_plan
    if total_biaya > budget_total:
        pengurangan = total_biaya - budget_total
        # Prioritas pengurangan dari destinasi dulu
        path_destinasi.sort(key=lambda x: destinasi[x])
        for d in path_destinasi:
            if destinasi[d] >= pengurangan:
                path_destinasi.remove(d)
                total_biaya -= destinasi[d]
                break
        # Jika masih perlu dikurangi, lanjut dari hidden gem
        if total_biaya > budget_total:
            path_hg.sort(key=lambda x: hidden_gem[x])
            for hg in path_hg:
                if hidden_gem[hg] >= pengurangan:
                    path_hg.remove(hg)
                    total_biaya -= hidden_gem[hg]
                    break

# Cetak hasil terbaik sebagai STRUK
if best_plan:
    print("\n===================================================")
    print("               RINCIAN BIAYA TOTAL           ")
    print("                 BATU TRIP 2025            ")
    print("===================================================")
    
    print(f"\n💰 Batas Budget Maksimal (Setelah Pengeluaran Tak Terduga): Rp{budget_total:,}")  
    print(f"⚠ Biaya Tak Terduga: Rp{biaya_tak_terduga:,}")

    print("\n🎢 DESTINASI:")
    for p in path_destinasi:
        print(f"- {p} (Rp{destinasi[p]:,})")

    print("\n🌿 HIDDEN GEM:")
    for hg in path_hg:
        print(f"- {hg} (Rp{hidden_gem[hg]:,})")

    print("\n🚗 TRANSPORTASI:")
    for t, harga in transportasi.items():
        print(f"- {t}: Rp{harga:,}")

    print("\n🍽 JAJANAN (include makan, minum, dan snack):")
    print(f"- Rp{jajanan:,}")

    print("\n🏨 HOTEL:")
    print(f"- Golden Tulip Batu (Rp{hotel['Golden Tulip Holland Resort Batu']:,})")

    print("\n======================================")
    print(f"💰 TOTAL BIAYA: Rp{total_biaya:,}")
    print("======================================")
    print(f"⏳ Waktu Eksekusi: {execution_time:.4f} detik")
else:
    print("❌ Tidak ada kombinasi yang memenuhi anggaran.")
    
#Dalam program ini, backtracking digunakan untuk mencari kombinasi 4 destinasi wisata dan minimal 1 hidden gem.
#Jika 4 destinasi dan minimal 1 hidden gem sudah dipilih, maka akan menghitung total biaya dan membandingkan dengan budget awal, lalu kembali untuk mencari kombinasi lain
#setelah mengecek kombinasi lainnya, dan dirasa melebihi dari budget, maka program akan menjalankan fungsi else pada fungsi (if best plan) dan sebelum mencetak, maka akan mencoba kombinasi lainnya
# kelebihan pendekatan backtracking : 
# 1. dapat lebih mudah menemukan solusi dengan optimal
# 2. Tidak menghitung kombinasi yang tidak diperlukan
# kekurangan pendekatan backtracking :
# 1. membutuhkan kompleksitas waktu yang tinggi, karena harus mencoba berbagai kombinasi
# 2. tidak selalu menemukan solusi jika tidak ada yang memenuhi syarat