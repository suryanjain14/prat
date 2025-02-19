# Trapping Rain Water
# Medium Accuracy: 42.45% Submissions: 100k+ Points: 4
# Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each
# block is 1. Compute how much water can be trapped in between blocks after raining.
#
# We can trap 2 units of water in the middle gap.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases
# follows. Each test case contains an integer N denoting the size of the array, followed by N space separated numbers to
# be stored in array.
#
# Output:
# Output the total unit of water trapped in between the blocks.
#
# Constraints:
# 1 <= T <= 100
# 3 <= N <= 107
# 0 <= Ai <= 108
#
# Example:
# Input:
# 2
# 4
# 7 4 0 9
# 3
# 6 9 9
#
# Output:
# 10
# 0
#
# Explanation:
# Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water
# trapped is 10 units.
#


def rainwater(array, n):
    tarea = 0
    maxra = [0] * n
    mx = array[-1]
    for i in range(n - 1, -1, -1):
        maxra[i] = max(array[i], mx)
        mx = max(maxra[i], mx)
    maxl = array[0]
    for i in range(n):
        maxl = max(maxl, array[i])
        maxr = maxra[i]
        carea = min(maxl, maxr) - array[i]
        tarea += carea if carea > 0 else 0

    print(tarea)


cases = int(input())
for _ in range(cases):
    n = int(input())
    array = list(map(int, input().split()))
    rainwater(array, n)
