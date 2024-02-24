class Kareler:

    def __init__(self, max1):
        self.max = max1
        self.sayi = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi < self.max:
            self.sayi += 1
            return self.sayi ** 2
        else:
            self.sayi = -1
            raise StopIteration


for i in Kareler(5):
    print(i)

iterator = iter(Kareler(5))
print(next(iterator))
print(next(iterator))
print(next(iterator))
