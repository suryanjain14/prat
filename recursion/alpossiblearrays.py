# Generate all possible sorted arrays from alternate elements of two given sorted arrays
#
# Given two sorted arrays A and B, generate all possible arrays such that first element is taken from A then from B then
# from A and so on in increasing order till the arrays exhausted. The generated arrays should end with an element from B.
#
# For Example
#
#
# A = {10, 15, 25}
# B = {1, 5, 20, 30}
#
# The resulting arrays are:
#   10 20
#   10 20 25 30
#   10 30
#   15 20
#   15 20 25 30
#   15 30
#   25 30

def allsortedarrays(array1, array2):
    c = [0] * (len(array2) + len(array1) + 1)

    def helper(a, b, c, i, j, k, l, o, flag):
        if flag:
            if o:
                print(c[:o + 1], o, c)
            for index in range(i, j):
                if not o:
                    c[o] = a[index]
                    helper(a, b, c, index + 1, j, k, l, o, not flag)
                else:
                    if a[index] > c[o]:
                        c[o + 1] = a[index]
                        helper(a, b, c, index + 1, j, k, l, o + 1, not flag)
        else:
            for index in range(k, l):
                if b[index] > c[o]:
                    c[o + 1] = b[index]
                    helper(a, b, c, i, j, index + 1, l, o + 1, not flag)

    helper(array1, array2, c, 0, len(array1), 0, len(array2), 0, True)


allsortedarrays([10, 15, 25], [1, 5, 20, 30])
