# def double(x):
#     return 2 * x
#
#
# y = map(double, [1, 2, 3, 4, 5, 6, 7])
# print(list(y))


print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])))
print(list(map(lambda x, y, z: x * y * z, [4, 5, 6, 7], [2, 3, 4, 5], [1, 2, 3, 4])))
print(list(map(lambda x: x + 1, [9, 10, 11, 12])))

