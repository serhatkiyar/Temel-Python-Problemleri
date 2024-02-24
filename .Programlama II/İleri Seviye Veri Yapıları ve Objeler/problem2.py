with open("C:/users/Serhat/Desktop/şiir.txt", "w", encoding="utf-8") as file:
    file.write("Memlekete bir sis çökmüş gece\n"
               "Usulca yanağıma sen düşüyorsun\n"
               "Sabah saat dokuzu beş geçe\n"
               "Terk edip bizleri gidiyorsun\n"
               "Ayrılık bu kadar yakmamıştı içimizi\n"
               "Farkında mısın bilmiyorum\n"
               "Aldın beraberinde cumhuriyetimizi\n"
               "Korkunç bir veda, sararmıştı her yer\n"
               "Ellerini uzat tutmak istiyoruz\n"
               "Masmavi gözleri kaybetmiş çocuk\n"
               "Aldı bir sabah ruhumuzu\n"
               "Lakin nasıl bölmesin yokluğun uykumuzu\n")

akros = ""
with open("C:/users/Serhat/Desktop/şiir.txt", "r", encoding="utf-8") as file:
    for i in file:
        akros += i[0]

print(akros)
