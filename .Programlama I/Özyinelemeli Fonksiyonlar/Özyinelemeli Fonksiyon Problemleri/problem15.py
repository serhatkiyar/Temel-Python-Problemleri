# 15. **Elemanları Belirli Bir Değere Kadar Olan Toplamları Bulma Fonksiyonu:**
# Belirli bir değere kadar olan sayıların toplamlarını hesaplayan özyinemeli bir fonksiyon yazın.

def alt_topla(lis, index, n=0, toplam=0):

    if n == len(lis):
        return toplam

    if lis[n] <= index:
        toplam += lis[n]

    return alt_topla(lis, index, n + 1, toplam)


liste = [1, 2, 2, 3, 4, 5, 6]
print(alt_topla(liste, 4))
