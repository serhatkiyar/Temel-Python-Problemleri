# Matrisin Sütunlarını Ortalamaya Göre Sıralama:
# Verilen bir matrisin sütunlarını ortalamaya göre küçükten büyüğe sıralayan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut Giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

sutunlar = []

for i2 in range(len(matris_1)):
    gecici_liste = []
    for j2 in range(len(matris_1[0])):
        gecici_liste.append(matris_1[j2][i2])
    sutunlar.append(gecici_liste)

sutun_ortalamalar = []
for u in sutunlar:
    toplam = 0
    for p in u:
        toplam += p
    sutun_ortalamalar.append(toplam/3)

print("Sütun ortalamaları=", sutun_ortalamalar)

for i3 in range(len(sutun_ortalamalar)):
    for j3 in range(len(sutun_ortalamalar) - i3 - 1):
        if sutun_ortalamalar[j3 + 1] > sutun_ortalamalar[j3]:
            sutunlar[j3 + 1], sutunlar[j3] = sutunlar[j3], sutunlar[j3 + 1]
            sutun_ortalamalar[j3 + 1], sutun_ortalamalar[j3] = sutun_ortalamalar[j3], sutun_ortalamalar[j3 + 1]

print(sutunlar)

for a in range(len(sutunlar)):
    for b in range(len(sutunlar[0])):
        matris_1[a][b] = sutunlar[b][a]

print("Sıralanmış Matris")
matrisciz(matris_1)

