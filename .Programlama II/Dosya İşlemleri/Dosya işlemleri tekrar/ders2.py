# Dosyalarda değişiklik yapma

with open("C:/Users/Serhat/Desktop/Dosya2.txt", 'w') as file:
    file.write("Serhat Kıyar\n")
    file.write("Umut Çalışkan\n")
    file.write("Muhammed Soner\n")
    file.write("İzzet Gündüz\n")

with open("C:/Users/Serhat/Desktop/Dosya2.txt", 'r+') as file:

    icerik = file.read()  # file.read() dosya içeriğimizin tek string biçiminde ki halidir.
    file.seek(0)  # İmleci girilen indexe götürür eğer imlecin gezindiği yerlerde başka karakterler varsa
    # yeni gelen karakterler üzerine yazılır.
    file.write("Muhammed Fatih Talu\n" + icerik)
