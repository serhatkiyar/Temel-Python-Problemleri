# 3. Bir listede belirli bir değeri arayın.

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

aranan_sayi = int(input("Hangi sayıyı arıyorsunuz: \n>>> "))

kontrol = False
for i in liste:
    if liste[i] == aranan_sayi:
        print(f"Aradığınız sayı {i}. index' te bulunuyor.")
        kontrol = True

if kontrol == False:
    print("Aradığınız sayı bulunamadı.")