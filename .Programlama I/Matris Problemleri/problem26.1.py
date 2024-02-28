# Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.
import random

def matrisciz(liste):
    print("Matris")
    for i in range(len(liste)):
        for j in range(len(liste[0])):
            print(liste[i][j], end=" ")
        print()

boyut = int(input("Boyut Gir: \n>>> "))

matris = [[random.choice([0, 1]) for i in range(boyut)] for x in range(boyut)]

matrisciz(matris)
alan = 0
for i in range(len(matris)):
    for j in range(len(matris[0])):
        if matris[i][j] == 1:
            alan += 1
print(alan)
