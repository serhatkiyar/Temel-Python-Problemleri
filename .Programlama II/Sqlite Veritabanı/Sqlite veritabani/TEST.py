import sqlite3

connect = sqlite3.connect("C:/users/Serhat/Desktop/database.db")
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS kütüphane (İSİM TEXT, YAZAR TEXT, YAYINEVİ TEXT, SAYFASAYİSİ TEXT)")
connect.commit()

# cursor.execute("INSERT INTO kütüphane VALUES('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', '561')")
# connect.commit()

# cursor.execute("SELECT * FROM kütüphane WHERE SAYFASAYİSİ = '712'")
# data = cursor.fetchall()

# for i in data:
#     print(i)

cursor.execute("UPDATE kütüphane SET SAYFASAYİSİ = '0' WHERE YAZAR = 'Ahmet Ümit'")
connect.commit()

cursor.execute("SELECT * FROM kütüphane")
data1 = cursor.fetchall()

for i in data1:
    print(i)
