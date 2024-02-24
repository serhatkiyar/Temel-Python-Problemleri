# 21. **Dizi Elemanlarını Toplamak İçin Özyinemeli Fonksiyon:**
# Bir dizinin elemanlarını toplamak için özyinemeli bir fonksiyon yazın.

def liste_toplam(lis, n=0, toplam=0):

    if n == len(lis):
        return toplam

    toplam += lis[n]

    return liste_toplam(lis, n + 1, toplam)


liste = [1, 2, 3, 4, 5]
print(liste_toplam(liste))
