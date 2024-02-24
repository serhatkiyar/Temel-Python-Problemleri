liste = []
pozitif_sayilar = []
negatif_sayilar = []
notr = []

sayi_adedi = int(input("Kaç adet sayı girmek istersiniz: "))


for i in range(1, sayi_adedi + 1):
    sayi = int(input("{}. sayıyı giriniz: ".format(i)))
    liste.append(sayi)
for i in liste:
    if i > 0:
        pozitif_sayilar.append(i)
    elif i < 0:
        negatif_sayilar.append(i)
    else:
        notr.append(i)

print("Oluşturulan listede {} adet pozitif sayı vardır.".format(len(pozitif_sayilar)))
print("Oluşturulan listede {} adet negatif sayı vardır.".format(len(negatif_sayilar)))
print("Oluşturulan listede {} adet 0 sayısı vardır.".format(len(notr)))
