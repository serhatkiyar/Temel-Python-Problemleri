# Matrisin Belirli Bir Satırındaki Elemanları Bölme:
# Verilen bir matrisin belirli bir satırındaki elemanları belirli bir sayıyla bölen bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

sec_satir = int(input("Hangi satır üzerinde işlem yapmak istersiniz: \n>>> "))
bolen_sayi = int(input(f"{sec_satir}. satırı hangi sayı ile bölmek istersiniz: \n>>> "))

for j1 in range(len(matris_1[0])):
    (matris_1[sec_satir][j1]) = float(str(matris_1[sec_satir][j1] / bolen_sayi)[:3])

print("Yeni Matris")
matrisciz(matris_1)
