# Bir Shape ana sınıfı ve ondan türeyen Triangle, Square ve Circle sınıflarını yazın.
# Her biri için alan ve çevre hesaplaması yapın.

from abc import abstractmethod


class Shape:
    def __init__(self, color, point_count):
        self.color = color
        self.pointCount = point_count

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, h, color, point_count):
        self.h = h
        super().__init__(color, point_count)

    def area(self):
        return self.h ** 2


class Triangle(Shape):
    def __init__(self, color, point_count, edge1, edge2, edge3):
        super().__init__(color, point_count)
        self.edge1, self.edge2, self.edge3 = edge1, edge2, edge3

    def area(self):
        s = (self.edge1 + self.edge2 + self.edge3) / 3
        area = (s * (s - self.edge1) * (s - self.edge2) * (s - self.edge3)) ** 0.5
        return area








