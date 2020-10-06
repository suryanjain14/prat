import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    k = 0
    j = 0
    su = 0
    ways = 0
    while k < len(s):
        t = k
        while j < m:
            print("as")
            su = su + s[t]
            t += 1
            j += 1
        if su == d:
            ways += 1
            print

        k +=  1

    return ways


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

    # fptr.close()
