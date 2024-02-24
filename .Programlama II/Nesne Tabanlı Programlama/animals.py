class Hayvan:

    def __init__(self, hayvanismi="Bilgi yok", ayaksayisi="Bilgi yok", kuyruk="Bilgi yok"):

        print("İnit fonksiyonu aktif.")
        self.isim = hayvanismi
        self.ayaksayisi = ayaksayisi
        self.kuyruk = kuyruk

    def bilgilerigoster(self):
        return self.isim, self.ayaksayisi, self.kuyruk


class Kus(Hayvan):

    def __init__(self, hayvanismi, ayaksayisi, kuyruk, renk="Bilgi yok"):

        super().__init__(hayvanismi, ayaksayisi, kuyruk)
        self.renk = renk


class At(Hayvan):

    def __init__(self, hayvanismi, ayaksayisi, kuyruk, hiz="Bilgi yok"):

        super().__init__(hayvanismi, ayaksayisi, kuyruk)
        self.hiz = hiz


leylek = Kus("leylek", "2", "0", "Beyaz")
arapati = At("at", "4", "0", "300")

print(leylek.renk, arapati.hiz)
print(leylek.bilgilerigoster())
print(arapati.bilgilerigoster())
