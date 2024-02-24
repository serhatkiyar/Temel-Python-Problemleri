# s adlı string değişkeninden noktalama işaretlerini kaldırarak ts adlı yeni bir string değişkenin üretiniz.

yazi = "Programlamada uzmanlaşmak isteyen bir kişinin çok sayida soru çözmesi gerekir! Bu aşamayi sadece sebatkâr öğrenciler geçer? İkinci problem sorunun anlaşilmasidir, Dikkatini verenler bu aşamayi rahatlikla geçer. Üçüncü aşamada anlaşilan sorunun çözüm basamaklarinin ortaya çikarilmasidir. Bir kâğit ve bir kalem bu güçlüğü aşmak için yeterlidir; Belirlenen çözüm basamaklarinin kod bloklarina dönüşümü en kolay aşama olarak görülür"

nok_isaretleri = [".", ":", ",", ";", "'", "!", "?", '"', ")", "("]
silinecekler = []
index = 0

for i in yazi:
    
    if i in nok_isaretleri:
        silinecekler.append(index)

    index += 1

yeniyazi = ""
a = 0

for i in silinecekler:
    yeniyazi += yazi[a:i]
    a = i + 1

print(yeniyazi)

