sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))
cift_sayilar = []
if sayi1 % 2 == 0 or sayi2 % 2 == 0 or sayi3 % 2 == 0:
    if sayi1 % 2 == 0:
        cift_sayilar.append(sayi1)
    if sayi2 % 2 == 0:
        cift_sayilar.append(sayi2)
    if sayi3 % 2 == 0:
        cift_sayilar.append(sayi3)
else:
    print("Girilen sayılar çift değildir...")
cift_sayilar.sort()
cift_sayilar.__reversed__()
if len(cift_sayilar) > 0:
    print("En küçük çift sayı= ", cift_sayilar[0])
