# 22. Bir listedeki elemanları belirli bir sayı kadar öteleme yaparak döndürün.


def kaydirsayi(lis, ks, kss):

    lis = lis[:ks] + lis[ks + 1:lis[ks + kss + 1]] + [lis[ks]] + lis[ks + kss + 1:]

    return lis


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(liste)

ks1 = int(input("Kaçıncı index' teki sayıyı kaydırmak istersiniz: \n>>> "))
kss1 = int(input(f"{liste[ks1]} kaç defa kaydırılacak: \n>>> "))

print(kaydirsayi(liste, ks1, kss1))
