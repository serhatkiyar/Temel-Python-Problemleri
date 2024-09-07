# Matristeki en büyük sayıyı bul.
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

diyagonaltoplam = 0

for i in range(len(matris)):

    for x in range(len(matris[0])):

        if i == x:
            diyagonaltoplam += matris[i][x]

print("\nDiyagonal Toplam\n", diyagonaltoplam, sep="")
