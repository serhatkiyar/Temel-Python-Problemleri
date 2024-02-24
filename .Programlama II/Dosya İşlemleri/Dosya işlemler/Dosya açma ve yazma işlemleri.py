file = open("C:/users/Serhat/Desktop/elektrik devreleri.txt", "w", encoding="utf-8")
file.write("Serhat Kıyar")
file.close()
file = open("C:/users/Serhat/Desktop/elektrik devreleri.txt", "a", encoding="utf-8")
file.write(" seni seviyorum.")
file.write(" <3\n")
for i in "Serhat seni seviyorum.":
    file.write(str(i) + "\n")
file.close()

with open("C:/users/Serhat/Desktop/elektrik devreleri.txt", "r", encoding="utf-8") as file:
    print(file.read())
