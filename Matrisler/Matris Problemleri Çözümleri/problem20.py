# Matrisin satır ve sütun toplamlarını hesapla.
import random


def matrisciz(liste):

    for i in range(len(liste)):

        for x in range(len(liste[0])):

            print(liste[i][x], end=" ")

        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[int(10*random.random()) for x in range(boyut)] for i in range(boyut)]
matrisciz(matris)

for i in range(len(matris)):

    satirtoplam = 0

    for j in range(len(matris[0])):
        satirtoplam += matris[i][j]

    print(satirtoplam, end=" ")

print()

for i in range(len(matris[0])):

    sutuntoplam = 0

    for j in range(len(matris)):

        sutuntoplam += matris[j][i]

    print(sutuntoplam, end=" ")
