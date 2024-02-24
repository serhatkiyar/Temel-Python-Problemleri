sayac = 1
sayi = ""
yenisayi = ""
while True:

    rakam = input(f"{sayac}. Sayıyı giriniz (Kaydetmek için 'q' tuşunu giriniz.): \n>>> ")
    if rakam == 'q':
        break
    elif 0 <= int(rakam) <= 9:
        sayi += rakam
    sayac += 1

for i in sayi[::-1]:
    yenisayi += i

print(yenisayi)
print(int(yenisayi)**0.5)

