olcu = int(input("olcu: \n>>> "))

for i in range(1, olcu):
    for j in range(i + int((i - 1) * (i - 2) / 2), i + int((i - 1) * (i - 2) / 2) + i):
        print(j, end=" ")
    print()