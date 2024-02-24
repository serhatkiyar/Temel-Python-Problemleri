mail_ek = ["@gmail.com", "@ogr.inonu.edu.tr", "@serhatkiyar.com", "@yahho.com"]
onaylimailler = []
with open("C:/users/Serhat/Desktop/mailler.txt", "r+", encoding="utf-8") as file:
    for mail in file:
        for i in mail_ek:
            if mail[:-1].endswith(i):
                onaylimailler.append(mail[:-1])
                continue

for i in onaylimailler:
    print(i)
