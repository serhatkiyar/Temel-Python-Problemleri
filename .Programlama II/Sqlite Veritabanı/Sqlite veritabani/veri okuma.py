import sqlite3

con = sqlite3.connect("C:/users/Serhat/Desktop(veritabanimm.db")
cursor = con.cursor()


def vericek():
    cursor.execute("Select * From tablo")
    data = cursor.fetchall()

    for i in data:
        for j in i:
            print(j, end=" ")
        print()


vericek()
