# Matristeki en büyük sayıyı bul.
import random

boyut = int(input("Matris boyutunu giriniz: \n>>> "))

matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
print(matris)

mak = matris[0][0]

for i in matris:

    for x in i:

        if x >= mak:
            mak = x

print(mak)
