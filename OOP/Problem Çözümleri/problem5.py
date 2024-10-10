# Bir Rectangle sınıfı oluşturun ve get_perimeter() metoduyla çevresini bulun.

class Rectang:
    def __init__(self, h_edge, v_edge):
        self.h_edge = h_edge
        self.v_edge = v_edge

    def get_perimeter(self):
        return 2*self.v_edge + 2*self.h_edge


dikdortgen = Rectang(4, 5)
print(dikdortgen.get_perimeter())

