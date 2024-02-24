liste = []
sayac = 0
while True:
    sayac += 1
    sayi = input(f"{sayac}. sayının tabanını giriniz: \n>>> ")
    sayius = input(f"{sayac}. sayının üssünü giriniz: >>> ")
    liste.append(int(sayi) ** int(sayius))
    bas = input("Kaydetmek için 'q' tuşuna basınız. Sayı eklemeye devam etmek için 'Enter' tuşuna basabilirsiniz. \n>>> ")
    if bas == 'q':
        break
index = 0
for i in liste:
    sayac = 0
    for x in liste:
        if i == x:
            sayac += 1
    if sayac == 1:
        print(i, index)
    index += 1

    