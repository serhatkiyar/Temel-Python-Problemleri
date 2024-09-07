# 21. Bir listedeki elemanları kaydırarak döndürün.

import random

liste = [random.randint(0, 50) for _ in range(20)]
print(liste)

dondur = int(input("Listeyi kaç kez kaydırmak istiyorsunuz: \n>>> "))

for i in range(dondur):
    liste = [liste[-1]] + liste[:-1]

print(liste)