# 20. **Dizi Elemanlarını Tek ve Çift Sayılara Ayırma Fonksiyonu:**
# Bir diziyi içindeki elemanları tek ve çift sayılara ayıran özyinemeli bir fonksiyon yazın.

def tek_cift_ayir(lis, n=0, listek=[], listcift=[]):

    if len(lis) == n:
        return listek, listcift

    if lis[n] % 2 == 0:
        listcift.append(lis[n])
        return tek_cift_ayir(lis, n + 1, listek, listcift)
    else:
        listek.append(lis[n]),
        return tek_cift_ayir(lis, n + 1, listek, listcift)


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tek_cift_ayir(liste))
