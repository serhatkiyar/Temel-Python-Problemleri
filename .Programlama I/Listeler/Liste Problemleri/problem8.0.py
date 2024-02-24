# 8. Bir listedeki tekrarlanan elemanları kaldırın.

import random

liste = [random.randint(0, 9) for _ in range(15)]
liste2 = []
print(liste)

for i in liste:
    if i not in liste2:
        liste2.append(i)

liste = liste2.copy()
print(liste)
