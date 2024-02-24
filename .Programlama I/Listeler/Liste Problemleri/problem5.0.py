# 5. Listenin en büyük ve en küçük elemanlarını bulun.

liste = [2, 4, 7, 3, 2, 75, 12, 74, 7, 3, 9]

minumum = liste[0]
maksimum = liste[0]

for i in liste:
    if maksimum < i:
        maksimum = i
    if minumum > i:
        minumum = i

print(f"maksimum= {maksimum} / minumum= {minumum}")
