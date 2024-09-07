import random

liste = [random.randint(0, 30) for _ in range(10)]
print(liste)

for i in range(int(len(liste)//2)):
    liste[i], liste[len(liste) - i - 1] = liste[len(liste) - i - 1], liste[i]

print(liste)