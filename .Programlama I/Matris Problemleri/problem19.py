# İki matrisin toplamını bul.
import random


def matrisciz(liste):

    for i in range(len(liste)):

        for x in range(len(liste[0])):

            print(liste[i][x], end=" ")

        print()


boyut = int(input("Matrisinizin boyutunu giriniz: \n>>> "))

matris1 = [[int(10*random.random()) for x in range(boyut)] for i in range(boyut)]
matrisciz(matris1)

matris2 = [[int(10*random.random()) for x in range(boyut)] for i in range(boyut)]
matrisciz(matris2)

matristoplam = [[0 for x in range(boyut)] for i in range(boyut)]
print("Matris toplamları")

for i in range(boyut):

    for j in range(boyut):

        matristoplam[i][j] = matris1[i][j] + matris2[i][j]

matrisciz(matristoplam)
