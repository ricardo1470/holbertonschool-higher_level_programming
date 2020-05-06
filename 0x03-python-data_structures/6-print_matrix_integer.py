#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print("")
    else:
        for i in (matrix):
            k = 0
            for j in i:
                if (k >= len(i) - 1):
                    print('{}'.format(j), end="")
                else:
                    print('{}'.format(j), end=" ")
                k = k + 1
            print("")
