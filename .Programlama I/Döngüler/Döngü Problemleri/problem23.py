# 23. Bir liste içindeki sayıları küçükten büyüğe sıralayan bir `for` döngüsü yazın.
# (Liste örneği: `[45, 12, 78, 23, 56]`)

liste = [45, 12, 78, 23, 56]
print(liste)

for i in range(len(liste)):
    for j in range(len(liste) - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

print(liste)
