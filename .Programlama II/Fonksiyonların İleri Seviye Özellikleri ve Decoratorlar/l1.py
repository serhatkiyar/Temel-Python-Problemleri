def topla(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam


# x = topla(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(x)

# def kisiler(**kwargs):
#     print(kwargs.items())
#     print(kwargs)
#     for i, j in kwargs.items():
#         print(f"İsim: {i} Soyisim: {j}")


# kisiler(serhat="Kıyar", x="y")

a = topla

print(type(a))
print(a(1, 2, 3))
