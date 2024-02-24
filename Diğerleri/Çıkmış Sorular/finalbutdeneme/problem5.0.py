def indeksbul(matris):
    mak = matris[0][0]
    indeksler = [(0, 0)]

    for i in range(len(matris)):
        for j in range(len(matris[0])):
            if matris[i][j] > mak:
                mak = matris[i][j]
                indeksler = [(i, j)]
            elif matris[i][j] == mak:
                indeksler.append((i, j))

    return mak, indeksler


matrix = [
    [1, 2, 2],
    [4, 4, 4],
    [2, 4, 3]
]

print(indeksbul(matrix))
