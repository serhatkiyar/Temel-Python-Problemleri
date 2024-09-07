# 6. Bir listedeki çift sayıları bulun.

import random

cift_sayilar = []
liste = [random.randint(1, 100) for _ in range(10)]
print(liste)

for i in liste:
    if i % 2 == 0 and i not in cift_sayilar:
        cift_sayilar.append(i)

print(cift_sayilar)
