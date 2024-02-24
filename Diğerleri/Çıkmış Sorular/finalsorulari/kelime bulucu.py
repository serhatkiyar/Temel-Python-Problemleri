yazi = "Programlamada uzmanlaşmak isteyen bir kişinin çok sayida soru çözmesi gerekir! Bu aşamayi sadece sebatkar öğrenciler geçer? İkinci problem sorunun anlaşilmasidir, Dikkatini verenler bu aşamayi rahatlikla geçer. Üçüncü aşamada anlaşilan sorunun çözüm basamaklarinin ortaya çikarilmasidir. Bir kâğit ve bir kalem bu güçlüğü aşmak için yeterlidir; Belirlenen çözüm basamaklarinin kod bloklarina dönüşümü en kolay aşama olarak görülür"
harfler = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'ı', 'o', 'p', 'ğ', 'ü', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Ğ', 'Ü', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ş', 'İ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Ö', 'Ç']
kelimeler = []
index = 0
sayac = 0
a = 0
indexler = []
for i in yazi:
    if i not in harfler:
        indexler.append(index)
    index += 1

for i in indexler:
    kelimeler.append(yazi[a:i])
    a = i + 1
    sayac += 1
kelimeler2 = []
for i in kelimeler:
    if i != '':
        kelimeler2.append(i)
print(kelimeler2)
print(indexler)