# 12. Kullanıcının girdiği iki sayı arasındaki sayıları ekrana yazdıran bir `for` döngüsü yazın.

sayi_1 = int(input("Birinci sayı giriniz: \n>>> "))
sayi_2 = int(input("İkinci sayıyı giriniz: \n>>> "))

if sayi_1 > sayi_2:
    sayi_1, sayi_2 = sayi_2, sayi_1

for i in range(sayi_1, sayi_2 + 1):
    print(i, end=" ")
    