# 18. **Dizi İçindeki En Küçük Elemanı Bulma Fonksiyonu:**
# Bir dizinin içindeki en küçük elemanı bulan özyinemeli bir fonksiyon yazın.

def en_kucuk(lis, mini=None, index=0):

    if len(lis) == index:
        return mini

    if mini == None or lis[index] < mini:
        mini = lis[index]

    return en_kucuk(lis, mini, index + 1)


liste = [2, 3, 1, 5, 6, 7, -9]
print(en_kucuk(liste))
