# Animal sınıfı oluşturun. Dog ve Cat sınıfları bu sınıftan türesin.
# Her birinin kendine özgü sound() metodunu oluşturun.

from abc import abstractmethod

class Animal:
    def __init__(self, foot_count):
        self.foot_count = foot_count

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, foot_count):
        super().__init__(foot_count)

    def sound(self):
        print("Hav Hav!")


class Cat(Animal):
    def __init__(self, foot_count):
        super().__init__(foot_count)

    def sound(self):
        print("Miyav Miyav!")



