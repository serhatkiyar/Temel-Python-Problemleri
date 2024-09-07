# 28. Bir liste içindeki elemanları tersten ekrana yazdıran bir `for` döngüsü yazın.
# (Liste örneği: `[10, 20, 30, 40, 50]`)

liste = [10, 20, 30, 40, 50]

for i1 in range(len(liste)):
    for j1 in range(len(liste) - i1 - 1):
        liste[j1], liste[j1 + 1] = liste[j1 + 1], liste[j1]

print(liste)

for i2 in range(len(liste)//2):
    liste[i2], liste[-(i2 + 1)] = liste[-(i2 + 1)], liste[i2]

print(liste)
