# **Palindrom Kontrolü Fonksiyonu:** Verilen bir string'in palindrom olup olmadığını kontrol eden özyinemeli bir
# fonksiyon yazın. (Palindrom, tersten okunduğunda aynı olan bir kelime, kelime grubu veya cümledir. )

def palindrom(kelime, n=0):
    if kelime[n] != kelime[-(n + 1)]:
        print("Bu kelime palindrom değildir.")
        return
    elif n + 1 == len(kelime):
        print("Bu kelime palindromdur.")
        return
    return palindrom(kelime, n + 1)


palindrom("efe")
