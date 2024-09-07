# Matrisin Satırlarını Ortalamaya Göre Sıralama:
# Verilen bir matrisin satırlarını ortalamaya göre küçükten büyüğe sıralayan bir Python programı yazın.
import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

ortalamalar = []
for i in matris_1:
    toplam = 0
    for j in i:
        toplam += j
    ortalamalar.append(toplam/len(matris_1[0]))
print("ortalamalar=", ortalamalar)

for i in range(len(ortalamalar)):
    for j in range(len(ortalamalar) - i - 1):
        if ortalamalar[j + 1] > ortalamalar[j]:
            matris_1[j + 1], matris_1[j] = matris_1[j], matris_1[j + 1]
            ortalamalar[j + 1], ortalamalar[j] = ortalamalar[j], ortalamalar[j + 1]

print("Sıralanmış Matris")
matrisciz(matris_1)

