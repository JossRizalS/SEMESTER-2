



print("nLOOPING IN PYTHON")
print("-------------------\n")
a = 0
b = float(input("Masukan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    a += 1 # increment3

print("\nPenggunaan Break pada Looping")
print("-------------------\n")
c = 0
d = float(input("Masukan angka anda : "))
while c < d: # a < b adalah syarat
    print(c)
    if c == 5: # Seleksi Kondisi
        break # Break Point
    c += 1 # Increment

print("\nPenggunaan Continue pada Looping")
print("-------------------\n")
e = 0
f = float(input("Masukan angka anda : "))
while e < f: # a < b adalah syarat
    print(e)
    if e == 5: # Seleksi Kondisi
        break # Break Point
    e += 1 # Increment

print("\nPenggunaan If else pada Looping")
print("-------------------\n")
a = 0
b = float(input("Masukan angka anda : "))
while a < b: 
    if a == (b - 1):
        print("Perulangan berhenti")
        break;
    else:
        print("Perulangan Ke - ", a)
        a += 1

