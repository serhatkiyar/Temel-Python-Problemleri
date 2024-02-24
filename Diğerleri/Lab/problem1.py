olcu = int(input("Olcu giriniz: \n>>> "))

for i in range(2*olcu):
    if i < olcu:
        print("* " * (i + 1))
    elif i > olcu:
        print("* " * (olcu - (i - olcu)))
