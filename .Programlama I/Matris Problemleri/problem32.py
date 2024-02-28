# Matrisin Sütunlarını Karıştırma:
# Verilen bir matrisin sütunlarını karıştıran bir Python programı yazın.

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

karistirilan_elemanlar = []

karis_sutun_1 = int(input("Karıştırmak istediğiniz 1. Sütunu giriniz: \n>>> "))
karis_sutun_2 = int(input("Karıştırmak istediğiniz 2. Sütunu giriniz: \n>>> "))

for x in range(len(matris_1)):
    for y in range(len(matris_1[0])):
        if y == karis_sutun_1 or y == karis_sutun_2:
            karistirilan_elemanlar.append(matris_1[x][y])

print("Sütunlar karıştırılırken kullanılacak elemanlar=", karistirilan_elemanlar)
for n in range(len(matris_1)):
    liste_eleman_tasiyici = []
    for m in range(len(matris_1[0])):
        if m != karis_sutun_1 and m != karis_sutun_2:
            liste_eleman_tasiyici.append(matris_1[n][m])
        else:
            a = random.choice(karistirilan_elemanlar)
            liste_eleman_tasiyici.append(a)
            karistirilan_elemanlar.remove(a)
    matris_2.append(liste_eleman_tasiyici)

print("Karıştırılmış Matrix")
matrisciz(matris_2)
