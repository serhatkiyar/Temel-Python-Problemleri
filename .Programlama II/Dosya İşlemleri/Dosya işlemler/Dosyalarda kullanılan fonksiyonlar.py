with open("bilgiler.txt", "r", encoding="utf-8") as file:
    file.seek(5)
    print(file.read(10))
    print(file.tell())
    file.seek(0)
    print(file.read(5))
