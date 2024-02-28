# Verilen sayıyı matrisin k. indeksine yerleştir?
import random


def matrisciz(liste):
    print("Matris")
    for i in range(len(liste)):
        for j in range(len(liste[0])):
            print(liste[i][j], end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
matrisciz(matris)

sayi = int(input("Yerleştirmek istediğiniz sayı: \n>>> "))
index = int(input("Hangi indexe yerleştirilecek: \n>>> "))
sayacindex = -1

for i in range(len(matris)):

    for x in range(len(matris[0])):

        sayacindex += 1

        if sayacindex == index:
            matris[i][x] = sayi

matrisciz(matris)
