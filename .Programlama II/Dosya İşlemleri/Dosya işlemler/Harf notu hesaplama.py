with open("C:/users/Serhat/Desktop/notlar.txt", "r", encoding="utf-8") as file:
    satirlar = file.readlines()
    ogrencinolar = []
    notlar = []
    for i in range(0, 3760, 19):
        ogrencinolar.append(satirlar[i][24:35])
    for i in range(12, 3760, 19):
        not1 = ""
        for n in satirlar[i][24:27]:
            if n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                not1 += n
        notlar.append(not1)

with open("C:/users/Serhat/Desktop/yeninotlar.txt", "w", encoding="utf-8") as file2:
    for i in range(len(ogrencinolar)):
        file2.write(f"{ogrencinolar[i]},{notlar[i]}\n")
