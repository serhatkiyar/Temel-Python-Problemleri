# 21. Kullanıcının girdiği bir sayının faktöriyelini bulan bir `while` döngüsü yazın.

sayi = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz: \n>>> "))

fak_sabit = 1
while sayi > 0:
    fak_sabit *= sayi
    sayi -= 1

print(fak_sabit)
