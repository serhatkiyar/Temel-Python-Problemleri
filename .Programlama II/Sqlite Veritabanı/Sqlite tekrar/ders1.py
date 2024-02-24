import sqlite3


veritabani = sqlite3.connect("C:/Users/Serhat/Desktop/Veritabanı.db")
cursor = veritabani.cursor()


def tabloolustur(tablo):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tablo} (İSİM TEXT, SOYİSİM TEXT, YAŞ TEXT)")
    veritabani.commit()


def veriekle(tablo, isim, soyisim, yas):

    cursor.execute(f"INSERT INTO {tablo} Values(?, ?, ?)", (isim, soyisim, yas))
    veritabani.commit()


def verisil(tablo, isim, soyisim, yas):
    cursor.execute(f"DELETE FROM {tablo} WHERE İSİM = ? AND SOYİSİM = ? AND YAŞ = ?", (isim, soyisim, yas))
    veritabani.commit()


def vericek(tablo):
    cursor.execute(f"Select * From {tablo}")
    data = cursor.fetchall()
    for i in data:
        print(i)


def yasguncelle(tablo, isim, soyisim, yeniyas):
    cursor.execute(f"UPDATE {tablo} SET YAŞ = ? WHERE İSİM = ? AND SOYİSİM = ?", (yeniyas, isim, soyisim))
    veritabani.commit()


def kisiara(tablo, isim, soyisim):
    cursor.execute(f"SELECT * FROM {tablo} WHERE İSİM = ? AND SOYİSİM = ?", (isim, soyisim))
    data = cursor.fetchall()
    for i in data:
        print(i)


tabloolustur("Öğrenciler")

veriekle("Öğrenciler", "Serhat", "Kıyar", "19")
veriekle("Öğrenciler", "Muhammed", "Soner", "19")
veriekle("Öğrenciler", "Umut", "Çalışkan", "24")
veriekle("Öğrenciler", "Efe", "Türkol", "19")

vericek("Öğrenciler")
print()

kisiara("Öğrenciler", "Umut", "Çalışkan")
print()

verisil("Öğrenciler", "Efe", "Türkol", "19")

vericek("Öğrenciler")
print()

veriekle("Öğrenciler", "Efe", "Türkol", "19")

vericek("Öğrenciler")
print()

yasguncelle("Öğrenciler", "Efe", "Türkol", "138759")

vericek("Öğrenciler")
