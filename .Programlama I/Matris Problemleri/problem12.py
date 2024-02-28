# *Matrisin Sıfıra Eşit Olup Olmadığını Kontrol Etme:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


boyut = int(input("Boyut gir: \n>>> "))

matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris)

matris_elemanlar = []
for i in range(len(matris)):
    for j in range(len(matris[0])):
        matris_elemanlar.append(matris[i][j])

for i in matris_elemanlar:
    if i != 0:
        print("Bu matris 0 matrisi değildir.")
        break
else:
    print("Bu matris 0 matrisidir.")
