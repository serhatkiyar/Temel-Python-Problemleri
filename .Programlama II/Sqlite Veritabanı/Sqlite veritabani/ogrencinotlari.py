import sqlite3

con = sqlite3.connect("C:/users/Serhat/Desktop/ogrencinotlari/veritabani.db")
cursor = con.cursor()


def tablo_olustur(tablo):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tablo} (ogrenci_no TEXT, puan TEXT)")
    con.commit()


tablo_olustur("ogrenci_notlari")


def veri_ekle(tablo, ogrencino, puan):
    cursor.execute(f"INSERT INTO {tablo} VALUES(?, ?)", (ogrencino, puan))
    con.commit()


def veri_al1(tablo):
    cursor.execute(f"SELECT * FROM {tablo}")
    data = cursor.fetchall()
    return data


def veri_al2(tablo):
    cursor.execute(f"SELECT ogrenci_no FROM {tablo}")
    data = cursor.fetchall()
    return data


def veri_al3(tablo, puan):
    cursor.execute(f"SELECT * FROM {tablo} WHERE puan = ?", (puan,))
    data = cursor.fetchall()
    return data


def lis_yazdir(liste):
    for i1 in liste:
        for j in i1:
            print(j, end=" ")
        print()


with open("C:/users/Serhat/Desktop/ogr_notlar.txt", "r", encoding="utf-8") as file:
    ogr_bilgi1 = []  # Ogrenci verileri dosyadan cekildi
    for i in file:
        ogr = i.split(",")
        ogr_bilgi1.append(ogr)

with open("C:/users/Serhat/Desktop/yeninotlar.txt", "r", encoding="utf-8") as file:
    ogr_bilgi2 = []  # Ogrenci verileri dosyadan cekildi
    for i in file:
        ogr = i.split(",")
        ogr_bilgi2.append(ogr)

# for i in ogr_bilgi:  # Ogrenci verileri tabloya girildi
#     veri_ekle("ogrenci_notlari", i[0], int(i[1]))
# print(ogr_bilgi)
# print(ogr_bilgi2)
# lis_yazdir(veri_al1("ogrenci_notlari"))
# lis_yazdir(veri_al2("ogrenci_notlari"))
# print(len(veri_al3("ogrenci_notlari", '60')))

# tablo_olustur("Yeni_Notlar")
ogr_bilgi1.sort()
ogr_bilgi2.sort()

ogrnumaralar2 = []
ogrnumaralar1 = []
for i in ogr_bilgi2:
    ogrnumaralar2.append(i[0])
for i in ogr_bilgi1:
    ogrnumaralar1.append(i[0])

for i in range(len(ogrnumaralar2)):
    if ogrnumaralar2[i] in ogrnumaralar1:
        numara = ogrnumaralar2[i]
        not1 = ogr_bilgi2[i][1]
        not2 = ogr_bilgi1[ogrnumaralar1.index(numara)][1]
        if not1 != not2:
            print(f"{numara} 1. --> {not2} 2. --> {not1}")

    else:
        print(f"{ogrnumaralar2[i]} listede bulunamadı!")

# for i in ogrnumaralar2:
#     sayac = 0
#     for j in ogrnumaralar2:
#         if i == j:
#             sayac += 1
#         if sayac == 2:
#             print(i)

