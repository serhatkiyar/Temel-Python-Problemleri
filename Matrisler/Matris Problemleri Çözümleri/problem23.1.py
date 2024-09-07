# Verilen sayıyı matrisin k. indeksine yerleştir?
import random


def matrixciz(liste):

    print("Matris")

    for i in range(len(liste)):

        for x in range(len(liste[0])):
            print(liste[i][x], end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
matrixciz(matris)

matristranspoz = [[0 for i in range(boyut)] for x in range(boyut)]

for i in range(len(matris)):

    for j in range(len(matris[0])):

        matristranspoz[i][j] = matris[j][i]

matrixciz(matristranspoz)
