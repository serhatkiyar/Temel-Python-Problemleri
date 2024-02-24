# 4. Bir listede belirli bir değeri kaç kez bulunduğunu sayın.

liste = [1, 2, 3, 4, 5, 1, 5, 8, 4, 3, 3, 0, 2, 5, 6]
sozluk = {}

for i in liste:
    sayac = 0
    for j in liste:
        if i == j:
            sayac += 1
    sozluk[i] = sayac

for u in range(len(sozluk) - 1):
    print(list(sozluk.keys())[u], sozluk[u])
