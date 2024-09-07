# *Matrisin Sütunlarını Sıralama:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


boyut = int(input("Boyut gir: \n>>> "))

print("Matris")
matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
matrisciz(matris)

islem_sutunu = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> ")) - 1
print(f"{islem_sutunu + 1}. sütundaki değerler sıralandı. \nYeni Matris")
liste_sutun = []

for i in range(len(matris)):
    liste_sutun.append(matris[i][islem_sutunu])

for i in range(len(liste_sutun)):
    for j in range(len(liste_sutun) - i - 1):

        if liste_sutun[j] > liste_sutun[j + 1]:
            liste_sutun[j], liste_sutun[j + 1] = liste_sutun[j + 1], liste_sutun[j]

for i in range(len(matris)):
    matris[i][islem_sutunu] = liste_sutun[i]

matrisciz(matris)
