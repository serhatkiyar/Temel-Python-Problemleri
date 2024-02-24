def harfnotubul(nott):
    if int(nott) >= 95:
        return "AA"
    elif int(nott) >= 90:
        return "AB"
    elif int(nott) >= 85:
        return "BA"
    elif int(nott) >= 80:
        return "BB"
    elif int(nott) >= 75:
        return "CB"
    elif int(nott) >= 70:
        return "CC"
    elif int(nott) >= 65:
        return "DC"
    elif int(nott) >= 60:
        return "DD"
    elif int(nott) >= 55:
        return "FD"
    else:
        return "FF"


file2 = open("C:/users/Serhat/Desktop/harnotlarii.txt", "w", encoding="utf-8")
with open("C:/users/Serhat/Desktop/veri1.txt", "r", encoding="utf-8") as file1:
    satirlar = file1.readlines()
    ogrencinolar = []
    harfnotlari = []
    for i in satirlar:
        ogrenci = i.split(",")
        file2.write(f"{ogrenci[0]}: {int(ogrenci[1][:-1]):3d} {harfnotubul(ogrenci[1])}\n")
