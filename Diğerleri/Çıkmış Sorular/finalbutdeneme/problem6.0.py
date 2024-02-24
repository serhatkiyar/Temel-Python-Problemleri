def karakterdegis(s):
    noktalama = ['!', '?', ',', '.', ':', ';', "'", '"', '(', ')']
    liste = list(s)

    for i in range(len(liste)):
        karakter = liste[i]
        if karakter in noktalama:
            liste[i] = '#'

    yenimetin = ""
    for i in liste:
        yenimetin += i
    return yenimetin


yazi = "Programlamada uzmanlaşmak isteyen bir kişinin çok sayida soru çözmesi gerekir! Bu aşamayi sadece sebatkâr öğrenciler geçer? İkinci problem sorunun anlaşilmasidir, Dikkatini verenler bu aşamayi rahatlikla geçer. Üçüncü aşamada anlaşilan sorunun çözüm basamaklarinin ortaya çikarilmasidir. Bir kâğit ve bir kalem bu güçlüğü aşmak için yeterlidir; Belirlenen çözüm basamaklarinin kod bloklarina dönüşümü en kolay aşama olarak görülür."
print(karakterdegis(yazi))
