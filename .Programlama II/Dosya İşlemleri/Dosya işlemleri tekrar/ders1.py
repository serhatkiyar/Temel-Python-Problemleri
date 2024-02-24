with open("C:/Users/Serhat/Desktop/dosya1.txt", "w") as file:  # 'w'
    file.write("Merhaba benim adım Serhat\n")
    for i in "Serhat":
        file.write(i + "\n")

with open("C:/Users/Serhat/Desktop/dosya1.txt", "a") as file:
    file.write("Hello")

with open("C:/Users/Serhat/Desktop/dosya1.txt", "r") as file:
    print(file.read())  # Tüm içeriği file.read() ile alırız. ( Tek bir string halinde.)
    for i in file:  # file üzerinde gezinmek istersek her iterasyonda file dosyasındaki bir satır alınır.
        print(i, end="")  # bunu aynı şekilde file.readlines() fonksiyonu elemanları satırlardan
        # oluşan bir listedir


