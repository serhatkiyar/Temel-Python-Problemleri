# 18. Bir listedeki elemanları belirli bir aralıkta kesin.

import random

liste = [random.randint(0, 100) for _ in range(20)]
print(liste)

a1 = int(input("Aralığın 1. indexi: \n>>> "))
a2 = int(input("Aralığın 2. indexi: \n>>> "))

if a1 > a2:
    a1, a2 = a2, a1

print(liste[a1:a2 + 1])
