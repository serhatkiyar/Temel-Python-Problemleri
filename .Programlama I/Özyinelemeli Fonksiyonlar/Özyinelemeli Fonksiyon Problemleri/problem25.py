# 25. **Elemanları Belirli Bir Değere Kadar Olan Fibonacci Serisi Fonksiyonu:**
# Fibonacci serisinin belirli bir değere kadar olan elemanlarını hesaplayan özyinemeli bir fonksiyon yazın.

def fibonacci(deger, x=1, y=1, fiboliste=[1]):
    if deger < 1:
        fiboliste

    if deger < y:
        return fiboliste

    fiboliste.append(y)

    return fibonacci(deger, x=y, y=x+y)


print(fibonacci(56))
