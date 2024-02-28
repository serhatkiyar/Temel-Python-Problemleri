# Matrisin Satırlarını Karıştırma:
# Verilen bir matrisin satırlarını karıştıran bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matris_2 = []
matrisciz(matris_1)

karis_satir_elemanlar = []


karis_satir1 = int(input("Karıştırmak istediğiniz 1. Satırı giriniz: \n>>> "))
karis_satir2 = int(input("Karıştırmak istediğiniz 2. Satırı giriniz: \n>>> "))

for i in range(len(matris_1)):
    for j in range(len(matris_1[0])):
        if i != karis_satir1 and i != karis_satir2:
            continue
        else:
            karis_satir_elemanlar.append(matris_1[i][j])
print("Satırlar karıştırılırken kullanılacak elemanlar=", karis_satir_elemanlar)

for i in range(len(matris_1)):
    liste_eleman_tasiyici = []
    for j in range(len(matris_1[0])):
        if i != karis_satir1 and i != karis_satir2:
            liste_eleman_tasiyici.append(matris_1[i][j])
        else:
            a = random.choice(karis_satir_elemanlar)
            liste_eleman_tasiyici.append(a)
            karis_satir_elemanlar.remove(a)
    matris_2.append(liste_eleman_tasiyici)

print("Karıştırılmış Matris: ")
matrisciz(matris_2)
