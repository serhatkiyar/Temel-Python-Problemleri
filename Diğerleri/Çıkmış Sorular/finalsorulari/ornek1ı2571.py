# N = 0 için Çıktı ne olur
def func(N):

    print(0)

    if 0 < 2:
            print(1)

            if 1 < 2:
                    print(2)

                    if 2 < 2:
                        func(2 + 1)

                    else:
                        print(2)

                    print(2)

            else:
                print(1)

            print(1)

    else:
        print(0)

    print(0)

# 0 1 2 2 2 1 0