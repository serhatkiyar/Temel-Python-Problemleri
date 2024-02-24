import sqlite3

veritabanim = sqlite3.connect("C:/users/Serhat/Desktop/ogrencinotlari/veritabani.db")
cursor = veritabanim.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS tablo (ogrencino TEXT, puan INT)")
# veritabanim.commit()


def notekle(ogrencino, puan):
    cursor.execute("INSERT INTO Yeni_Notlar VALUES(?, ?)", (ogrencino, puan))
    veritabanim.commit()


# while True:
#     islem = input("Çıkmak için 'q' giriniz. Devam etmek için Enter basınız. \n>>> ")
#     if islem == "q":
#         break
#     ogrencino1 = input("Öğrenci No: ")
#     puan1 = input("Puan: ")
#     notekle(ogrencino1, puan1)


def vericek():
    veritabanim.execute("Select * From Yeni_Notlar")
    data = cursor.fetchall()
    print(data)
    for i in data:
        for j in i:
            print(j, end=" ")
        print()


vericek()
veritabanim.close()
