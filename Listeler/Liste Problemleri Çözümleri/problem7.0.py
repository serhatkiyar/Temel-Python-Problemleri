# 7. Liste elemanlarını toplayın.

import random

liste = [random.randint(1, 100) for _ in range(5)]
print(liste)

toplam = 0

for i in liste:
    toplam += i

print(toplam)