# 22. **Dizi Elemanlarının Faktöriyelini Hesaplama Fonksiyonu:**
# Bir dizinin elemanlarının faktöriyelini hesaplayan özyinemeli bir fonksiyon yazın.

def liste_faktoriyel(lis, m=1, n=0, faktoriyel=1):

    if n == len(lis):
        return lis

    if lis[n] >= m:
        faktoriyel *= m
        return liste_faktoriyel(lis, m + 1, n, faktoriyel)
    else:
        lis[n] = faktoriyel
        return liste_faktoriyel(lis, 1, n + 1, 1)


liste = [1, 2, 3, 4, 5]
print(liste_faktoriyel(liste))
