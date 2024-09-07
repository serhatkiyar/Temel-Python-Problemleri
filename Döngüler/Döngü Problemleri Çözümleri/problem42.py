# Tam bölen bulma programı

liste = []

sayi = int(input("Bir sayı giriniz: "))


for i in range(1, sayi):
    if sayi % i == 0:
        liste.append(i)


print(liste)
