# 25. Kullanıcının girdiği bir sayının tek mi çift mi olduğunu
# kontrol eden bir `if` ve `else` kullanarak bir program yazın.

def tekcift(x):
    if x % 2 == 0:
        return 0
    return 1


sayi = int(input("Bir sayı giriniz: \n>>> "))
print(tekcift(sayi))