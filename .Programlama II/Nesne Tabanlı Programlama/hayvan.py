class Hayvan:
    def __init__(self, hayvan_ismi="bilgi yok", bacak_sayisi="bilgi yok", kuyruk="bilgi yok"):
        print("Hayvan init aktif")
        self.hayvanismi = hayvan_ismi
        self.bacaksayisi = bacak_sayisi
        self.kuyruk = kuyruk

    def bilgilerigoster(self):
        print("""
        Hayvan İsmi: {}
        Bacak Sayısı: {}
        Kuyruğu Var Mı: {}
        """.format(self.hayvanismi, self.bacaksayisi, self.kuyruk))


aslan = Hayvan("Aslan", "4", "var")
aslan.bilgilerigoster()


class Kopek:
    def __init__(self, hayvan_ismi="bilgi yok", bacak_sayisi="bilgi yok",
                 kuyruk="bilgi yok", havlama_gucu="bilgi yok"):
        print("Aslan init aktif")
        self.hayvanismi = hayvan_ismi
        self.bacaksayisi = bacak_sayisi
        self.kuyruk = kuyruk
        self.havlamagucu = havlama_gucu

    def bilgilerigoster(self):
        print("""
        Hayvan ismi: {}
        Bacak sayısı: {}
        Kuyruğu var mı: {}
        Havlama gücü: {}
        """.format(self.hayvanismi, self.bacaksayisi, self.kuyruk, self.havlamagucu))


doberman = Kopek("Doberman", "4", "var", "300")
doberman.bilgilerigoster()
