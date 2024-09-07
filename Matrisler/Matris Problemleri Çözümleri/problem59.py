# Matrisin Belirli Bir Satırındaki Elemanları Toplama:
# Verilen bir matrisin belirli bir satırındaki elemanları toplayan bir Python programı yazın.

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

toplam = 0

for j1 in range(len(matris_1[sec_satir])):
    toplam += matris_1[sec_satir][j1]
print(f"{sec_satir}. satır toplamı= {toplam}")
