# Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.
def matrisciz(liste):
    print("Matris")
    for i in range(len(liste)):
        for j in range(len(liste[0])):
            print(liste[i][j], end=" ")
        print()


N = int(input("Boyut(N) giriniz: \n>>> "))
matris = [[i for i in range(x + 1 - N, x + 1)] for x in range(N, N**2 + 1, N)]
matrisciz(matris)
 