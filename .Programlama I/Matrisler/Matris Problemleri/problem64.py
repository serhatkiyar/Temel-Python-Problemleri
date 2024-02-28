# Matrisin Belirli Bir Sütunundaki Elemanları Güçlendirme:
# Verilen bir matrisin belirli bir sütunundaki elemanları belirli bir sayıyla
# kuvvetine yükselten bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istiyorsunuz: \n>>> "))
kuvvet = int(input(f"{sec_sutun}. sütunun alınacağı kuvvet değerini giriniz: \n>>> "))

for j1 in range(len(matris_1)):
    matris_1[j1][sec_sutun] **= kuvvet

print("Yeni Matris")
matrisciz(matris_1)
