names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
surnames = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]
people = []
kisiler = zip(names, surnames)
print(list(kisiler))
for i, j in zip(names, surnames):
    people.append(i + " " + j)
people.sort()
for i in people:
    print(i)
