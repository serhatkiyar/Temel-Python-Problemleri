liste = [1, 2, 3, 4, 5]

print(type(liste))

iterasyon = iter(liste)

while True:
    try:
        print(next(iterasyon))
    except StopIteration:
        print("İterasyon Tamamlandı")
        break
# ['ATV', 'Fox', 'Tv8', 'Show TV']

class Kumanda:

    def __init__(self, kanallar):
        self.kanallar = kanallar
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.kanallar[self.index]


kumanda = Kumanda(['ATV', 'Fox', 'Tv8', 'Show TV'])
iterasyon = iter(kumanda)
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))

liste = [1, 2, 3, 4, 5]

print(type(liste))

iterasyon = iter(liste)
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))

print(type(iterasyon))
class Iterable:
    def __init__(self, *args):
        self.args = args
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.args):
            return self.args[self.index]
        else:
            self.index = -1
            raise StopIteration

    def __len__(self):
        return len(self.args)

    def __str__(self):
        return str(self.args)


rakamlar = Iterable(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

iterator = iter(rakamlar)

for i in rakamlar:
    print(i, end=" ")
print()
for i in range(3):
    print(next(iterator), end=" ")
print("*", next(iterator))



