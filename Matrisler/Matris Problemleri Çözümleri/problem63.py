# Matrisin Belirli Bir Satırındaki Elemanları Güçlendirme:
# Verilen bir matrisin belirli bir satırındaki elemanları belirli bir sayıyla kuvvetine yükselten bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris)

sec_satir = int(input("Hangi satır üzerinde işlem yapmak istiyorsunuz: \n>>> "))

kuvvet = int(input(f"{sec_satir}. satırın alınacağı kuvvet değerini giriniz: \n>>> "))

for j1 in range(len(matris[0])):
    matris[sec_satir][j1] **= kuvvet

print("Yeni Matris")
matrisciz(matris)
