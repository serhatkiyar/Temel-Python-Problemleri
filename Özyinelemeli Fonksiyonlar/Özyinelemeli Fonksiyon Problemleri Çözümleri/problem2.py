# # 2. **Fibonacci Serisi Hesaplama Fonksiyonu:**
# # Fibonacci serisinin n'inci elemanını hesaplayan özyinemeli bir fonksiyon yazın.

def fibonacci(n, x=1, y=1):
    if n == 2:
        return y
    return fibonacci(n - 1, x=y, y=x+y)


print(fibonacci(7))
