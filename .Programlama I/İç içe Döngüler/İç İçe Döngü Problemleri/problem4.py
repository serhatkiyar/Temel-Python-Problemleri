olcu = int(input("olcu: \n>>> "))

for i in range(1, olcu + 1):
    print("", i, end=" ")
print("\n +" + olcu*olcu*"_", end="")
print()

for i in range(1, olcu + 1):
    print(i, "|", end=" ")
    for j in range(1, olcu*olcu + 1):
        print(i*j, end=" ")
        if j % 10 == 0:
            print()
            break
