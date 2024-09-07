# 14. Liste elemanlarını rastgele sıralayın.

import random

liste = [i for i in range(0, 10)]
print(liste)
indexler = [i2 for i2 in range(len(liste))]
liste2 = []

for i in range(len(liste)):
    index = random.choice(indexler)
    liste2.append(liste[index])
    indexler.remove(index)

liste = liste2.copy()

print(liste)




