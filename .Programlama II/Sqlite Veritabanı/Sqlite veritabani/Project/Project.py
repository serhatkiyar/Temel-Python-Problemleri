import sqlite3

connect = sqlite3.connect("Bakanlik.db")
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (İSİM TEXT, YAZAR TEXT, YAYINEVİ TEXT, BASKİ TEXT, SAYFASAYİSİ TEXT)")
connect.commit()


class Kitap:
    def __init__(self, isim, yazar, yayinevi, baski, sayfasayisi):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.baski = baski
        self.sayfasayisi = sayfasayisi

    def __str__(self):
        return f"Kitap İsmi: {self.isim} \nYazar: {self.yazar} \nYayınevi: {self.yayinevi} \nBaskı: {self.baski} \nSayfa Sayısı: {self.sayfasayisi} "


class Kutuphane:



    def baglantikapat(self):
        connect.close()

    def baglantikur(self):
        connect = sqlite3.connect("Bakanlik.db")
        cursor = connect.cursor()

    def kitap_ekle(self, kitap):
        cursor.execute("INSERT INTO kitaplar VAlUES(?, ?, ?, ?, ?)", (kitap.isim, kitap.yazar, kitap.yayinevi, kitap.baski, kitap.sayfasayisi))
        connect.commit()

    def kitap_sil(self, kitap):
        cursor.execute("DELETE FROM kitaplar WHERE İSİM = ?", (kitap.isim,))
        connect.commit()

    def baski_arttir(self, kitap):
        cursor.execute("UPDATE FROM kitaplar SET BASKİ = +1 WHERE İSİM = ?", (kitap.isim,))
        connect.commit()

    def yayinevi_degistir(self, kitap, yayinevi):
        cursor.execute("UPDATE FROM kitaplar SET YAYINEVİ = ? WHERE İSİM = ?", (yayinevi, kitap.isim))
        connect.commit()

    def verial(self):
        cursor.execute("SELECT * FROM kitaplar")
        data = cursor.fetchall()
        return data

    def kitapara(self, kitap):
        cursor.execute("SELECT * FROM kitaplar WHERE İSİM = ?", (kitap.isim,))
        data = cursor.fetchall()
        return data


def datayaz(data):
    for i in data:
        print(i)



kutuphane = Kutuphane
kitap1 = Kitap("programalama", "Talu", "inonu", "24", 672)
print(kitap1)
kutuphane.kitap_ekle(kutuphane, kitap1)
datayaz(kutuphane.verial(kutuphane))
