alfabeb = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Ğ', 'Ü', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ş', 'İ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Ö', 'Ç']
alfabek = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'ı', 'o', 'p', 'ğ', 'ü', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç']


def degistir(yazi):
    yazi2 = ""
    yazi3 = ""
    for i in yazi:
        if i in alfabeb:
            yazi2 += i
        if i in alfabek:
            yazi3 += i

    return yazi2 + yazi3


yaz = "Merhaba Arkadaşlar Ben Burak Oyunda"
print(degistir(yaz))
