# 17. **Dizi İçindeki En Büyük Elemanı Bulma Fonksiyonu:**
# Bir dizinin içindeki en büyük elemanı bulan özyinemeli bir fonksiyon yazın.

def listenin_buyugu(lis, n=0, mak=None):

    if n == len(lis):
        return mak

    if mak == None or lis[n] >= mak:
        mak = lis[n]

    return listenin_buyugu(lis, n + 1, mak)


liste = [1, 2, 3, 4, 5, 6, 7, 8]
print(listenin_buyugu(liste))
