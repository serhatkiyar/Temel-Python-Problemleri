sayi = input("Bir sayı giriniz: ")
liste = []
toplam = 0
def faktoriyel_bulucu(x):
    fak_sabit = 1
    if x == 0:
        return 1
    for i in range(1, x+1):
        fak_sabit *= i
    return fak_sabit
for i in sayi:
    liste.append(faktoriyel_bulucu(int(i)))
for i in liste:
    toplam += i
if int(sayi) == toplam:
    print("Bu sayı güçlü sayıdır.")
else:
    print("Bu sayı güçlü sayı değildir")
print(0) + 1
