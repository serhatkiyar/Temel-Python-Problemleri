# 24. 1 ile 10 arasındaki sayıların kareköklerini ekrana yazdıran bir `for` döngüsü yazın.

def karakok(x):
    return x ** 0.5


for i in range(1, 10 + 1):
    print(karakok(i))
    