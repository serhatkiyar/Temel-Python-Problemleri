# n sayısına kadar olan çift sayıların çarpımı tek sayılarını toplamı

cift_sayilar = []
cift_carpim = 1
tek_toplam = 0
tek_sayilar = []

islem_sayisi = int(input("Hangi sayıya kadar işlem yapmak istersiniz: "))


for i in range(1, islem_sayisi):
    if i % 2 == 0:
        cift_sayilar.append(i)
    else:
        tek_sayilar.append(i)
for i in cift_sayilar:
    cift_carpim *= i
for i in tek_sayilar:
    tek_toplam += i
print("çiftsayılarçarpımı ", cift_carpim)
print("teksayılartoplamı ", tek_toplam)
