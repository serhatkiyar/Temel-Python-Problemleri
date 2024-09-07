# 8. **Dizi Elemanlarını Ters Çevirme Fonksiyonu:**
# Bir dizinin elemanlarını ters çeviren özyinemeli bir fonksiyon yazın.

def terscevir(lis, n=0):

    lis[n], lis[-1 * (n + 1)] = lis[-1 * (n + 1)], lis[n]

    if n + 1 == len(lis)//2:
        return lis

    return terscevir(lis, n + 1)


liste = [1, 2, 3, 4, 5, 6]
print(liste)
print(terscevir(liste))
