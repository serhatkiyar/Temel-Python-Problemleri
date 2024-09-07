# 12. **Dizi Elemanlarının Ortalamasını Hesaplama Fonksiyonu:**
# Bir dizinin elemanlarının ortalamasını hesaplayan özyinemeli bir fonksiyon yazın.

def lis_ort(lis, n=0):
    if n == len(lis):
        return 0
    return lis[n]/len(lis) + lis_ort(lis, n + 1)


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(lis_ort(liste))
