# 12. Liste elemanlarını birleştirip bir string oluşturun.

import random

liste = [random.randint(0, 9) for _ in range(25)]
print(liste)
yazi = ""

for i in liste:
    yazi += str(i)

print(yazi)
