# 19. **Elemanları Belirli Bir Değere Kadar Olan Sayıları Çarpan Fonksiyon:**
# Belirli bir değere kadar olan sayıların çarpımını hesaplayan özyinemeli bir fonksiyon yazın.

def alt_carp(lis, deger, n=0, carpim=1):

    if n == len(lis):
        return carpim

    if lis[n] <= deger:
        carpim *= lis[n]

    return alt_carp(lis, deger, n + 1, carpim)


liste = [1, 2, 3, 4, 5]
print(alt_carp(liste, 4))
