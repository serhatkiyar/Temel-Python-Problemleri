# Matrisin Belirli Bir Sütunundaki Elemanları Toplama:
# Verilen bir matrisin belirli bir sütunundaki elemanları toplayan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

toplam = 0

sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> "))

for i1 in range(len(matris_1)):
    toplam += matris_1[i1][sec_sutun]

print(f"{sec_sutun}. sütun toplamı= {toplam}")
