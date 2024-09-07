# 31. Girilen cümlenin hangi harfin kaç defa tekrarlandığı

sozluk = {}

yazi = input("Bir yazı giriniz: ")


for i in yazi:
    sozluk[i] = "kontrol"
for i in sozluk:

    sayac = 0

    for x in yazi:

        if i == x:
            sayac += 1

    print(i, "Sayısı", sayac, "kadar tekrarlanmıştır.")
