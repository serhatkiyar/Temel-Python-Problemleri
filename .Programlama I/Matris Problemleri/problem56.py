# Matrisin Belirli Bir Sütunundaki Elemanları Bölme:
# Verilen bir matrisin belirli bir sütunundaki elemanları belirli bir sayıyla bölen bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> "))
bolen_sayi = int(input(f"{sec_sutun}. sütunu hangi sayı ile bölmek istersiniz:\n>>> "))

for i1 in range(len(matris_1)):
    (matris_1[i1][sec_sutun]) = float(str(matris_1[i1][sec_sutun] / bolen_sayi)[:3])

print("Yeni Matris")
matrisciz(matris_1)
