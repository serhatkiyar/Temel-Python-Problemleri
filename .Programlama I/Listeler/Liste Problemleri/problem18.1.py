# 18. Bir listedeki elemanları belirli bir aralıkta kesin.

import random

liste = [random.randint(1, 100) for _ in range(20)]
print(liste)
aralik = []

a1 = int(input("Aralığın 1. indexi: \n>>> "))
a2 = int(input("Aralığın 2. indexi: \n>>> "))

if a1 > a2:
    a1, a2 = a2, a1

for i in range(len(liste)):

    if a1 <= i <= a2:
        aralik.append(liste[i])

print(aralik)

