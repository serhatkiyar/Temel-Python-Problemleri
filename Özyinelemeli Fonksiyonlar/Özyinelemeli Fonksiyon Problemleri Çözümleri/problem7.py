# 7. **Eleman Sayısını Bulma Fonksiyonu:**
# Bir dizinin eleman sayısını hesaplayan özyinemeli bir fonksiyon yazın.

def dizi_eleman(liste, n=0):
    print(liste)
    if len(liste) == 0:

        return n

    return dizi_eleman(liste[n:], n + 1)


liste1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(dizi_eleman(liste1))
