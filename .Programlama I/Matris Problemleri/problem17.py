# *Matrisin Sütunlarını Kopyalama:*
import random


def matrixciz(matris):
    for i in matris:
        for j in i:
            print(j, end= " ")
        print()


boyut = int(input("Boyut gir: \n>>> "))
matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrixciz(matris)

kopya_sutun = int(input("Hangi sütunu kopyalamak istersiniz: \n>>> "))
yapistir_sutun = int(input("Hangi sütuna yapıştırmak istersiniz: \n>>> "))

for j in range(len(matris)):
    matris[j][yapistir_sutun - 1] = matris[j][kopya_sutun - 1]

matrixciz(matris)