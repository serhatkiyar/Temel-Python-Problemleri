olcu = int(input("olcu: \n>>> "))
for j in range(olcu):
    print(" " * ((olcu - j) + (int(-2 * (j/(j + 1) - 0.5)))) + "*" + " " * (2 * j + 1) + "*" * int((j/(j + 1) + 0.5)))

