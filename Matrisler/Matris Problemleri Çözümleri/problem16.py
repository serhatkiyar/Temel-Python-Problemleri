# *Matrisin Satırlarını Kopyalama:*
import random


def matrixciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end= " ")
        print()


boyut = int(input("Boyut gir: \n>>> "))

matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrixciz(matris)

kopya_satir = int(input("Kaçıncı satırı kopyalıyacaksın: \n>>> "))
yapistir_satir = int(input("Kaçıncı satıra yapıştıracaksın: \n>>> "))

for i in range(len(matris)):
    matris[yapistir_satir - 1][i] = matris[kopya_satir - 1][i]

matrixciz(matris)