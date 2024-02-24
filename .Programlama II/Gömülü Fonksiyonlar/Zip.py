liste1 = [1, 2, 3, 4, 5, 6, 7, 8]
liste2 = [5, 4, 3, 2, 1]
sonuc = list()
i = 0
while len(liste1) > i and len(liste2) > i:

    sonuc.append((liste1[i], liste2[i]))
    i += 1

print(sonuc)

print(list(zip(liste1, liste2)))

for i, j in zip(liste1, liste2):
    print(i, j)
