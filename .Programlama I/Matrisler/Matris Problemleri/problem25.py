# İki matrisin çarpımını hesaplayan prog?
import random


def matrisciz(liste):

    print("Matris")

    for i in range(len(liste)):

        for x in range(len(liste[0])):

            print(liste[i][x], end=" ")

        print()


boyut = int(input("Boyut gir: \n>>> "))

matris1 = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
matrisciz(matris1)

matris2 = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
matrisciz(matris2)

matris3 = [[0 for i in range(boyut)] for x in range(boyut)]

for i in range(len(matris1)):

    for j in range(len(matris1[0])):

        matris3[i][j] = matris1[i][j] * matris2[i][j]

matrisciz(matris3)
