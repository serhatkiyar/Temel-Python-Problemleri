sayi1 = int(input("Birinci sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))
sayi3 = int(input("Üçüncü sayıyı giriniz:"))

if sayi1 % 2 == 0:
    if sayi1 % 2 == 0 and sayi2 % 2 == 0 and sayi3 % 2 == 0:
        if sayi1 < sayi2 and sayi1 < sayi3:
            print("En küçük çift sayı= ", sayi1)
        if sayi2 < sayi1 and sayi2 < sayi3:
            print("En küçük çift sayı= ", sayi2)
        if sayi3 < sayi1 and sayi3 < sayi2:
            print("En küçük çift sayı= ", sayi3)
elif sayi2 % 2 == 0:
    if sayi3 % 2 == 0:
        if sayi2 < sayi3:
            print("En küçük çift sayı= ", sayi2)
        else:
            print("En küçük çift sayı= ", sayi3)
    else:
        print("En küçük çift sayı= ", sayi2)
elif sayi3 % 2 == 0:
    print("En küçük çift sayı= ", sayi3)
else:
    print("Çift sayı gir ki sana küçük olanı söyliyim...")
