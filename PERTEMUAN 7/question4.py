belanjaan = {
   "Apel": {"harga":5000, "jumlah":10},
   "Jeruk": {"harga":3000, "jumlah":5},
    "Mangga": {"harga":7000, "jumlah":7},
    "Pisang": {"harga":2000, "jumlah":20},
    "Semangka": {"harga":15000, "jumlah":1},
}


# Menghitung tota belanjaan ibu sari
total_belanja = 0
for buah, info in belanjaan.item():
    total_harga = info["harga"] * info["jumlah"]
    total_belanja += total_harga
    print(f"Total harga {buah}: Rp{total_harga}")

print("Total Belanjaan ibu sari adalah: Rp", total_belanja)