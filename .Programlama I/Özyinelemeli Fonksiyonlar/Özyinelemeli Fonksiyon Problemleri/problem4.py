# 4. **Dizi Elemanlarının Toplamını Hesaplama Fonksiyonu:**
# Bir dizi içindeki elemanların toplamını hesaplayan özyinemeli bir fonksiyon yazın.

def listetopla(liste, n=0):
    if len(liste) == n:
        return 0

    return liste[n] + listetopla(liste, n + 1)


liste1 = [1, 2, 3, 4, 5]
print(listetopla(liste1))
