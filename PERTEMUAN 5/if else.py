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