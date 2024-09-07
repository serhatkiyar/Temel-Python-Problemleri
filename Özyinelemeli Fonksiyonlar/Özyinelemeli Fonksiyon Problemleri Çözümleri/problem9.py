# Bir diziyi sıralayan özyinemeli bir sıralama algoritması fonksiyonu yazın.
# 9. **Dizi Elemanlarını Sıralama Fonksiyonu:**

def sirala_lis(lis, m=0, n=0):

    if n + 1 == len(lis):
        return sirala_lis(lis, m + 1, n=0)

    if m == len(lis):
        return lis

    if lis[n] > lis[n + 1]:
        lis[n], lis[n + 1] = lis[n + 1], lis[n]

    return sirala_lis(lis, m, n + 1)


liste = [1, 6, 2, 9, 4, 33, 77, 1, 2, 8]
print(sirala_lis(liste))
