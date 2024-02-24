import math
n = int(input("Kaçıncı satır: "))

for j in range(0, n + 1):
    print(" "*(n - j), end="")
    for i in range(j + 1):
        print(int(math.factorial(j)/math.factorial(j - i)/math.factorial(i)), end=" ")
    print()
