olcu = int(input("olcu: \n>>> "))

for i in range(1, olcu*olcu + 1):
    print(i, end="  ")
    if i % olcu == 0:
        print()
