with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    icerik = file.read()
    icerik = "Mehmet Keper\n" + icerik
    file.seek(0)
    file.write(icerik)
    print(file.read())

with open("bilgiler.txt", "r", encoding="utf-8") as file:
    print(file.read())
