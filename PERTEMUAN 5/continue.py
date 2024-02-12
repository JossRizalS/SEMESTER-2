print("\nPenggunaan Break pada Looping")
print("-------------------\n")
a = 0
b = float(input("Masukan angka anda : "))
while a < b: # a < b adalah syarat
    a += 1 # increment
    if a == 5: # Seleksi Kondisi
        continue # Continue Point
    print(a)