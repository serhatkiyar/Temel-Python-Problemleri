file = open("C:/users/Serhat/Desktop/Read Me.txt", "w", encoding="utf-8")

for i in "Serhat seni seviyorum.":
    file.write(str(i) + "\n")

file.close()

file = open("C:/users/Serhat/Desktop/Read Me.txt", "r", encoding="utf-8")

for i in file:
    print(i)

file.close()

file = open("C:/users/Serhat/Desktop/Read Me.txt", "r", encoding="utf-8")

for _ in range(6):
    print(file.readline()[:-1], end="")

file.close()

print()

file = open("C:/users/Serhat/Desktop/Read Me.txt", "r", encoding="utf-8")

liste = file.readlines()
print(liste)
print("_________")
print(liste[0][-2])
print("_________", end="")
# for i in liste:
#     for j in i[:-1]:
#         print(j,end="")
