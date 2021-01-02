# Find all even length binary sequences with same sum of first and second half bits
#
# Given a number n, find all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
#
# Examples:
#
# Input:  N = 2
# Output:
# 0101 1111 1001 0110 0000 1010
#
# Input:  N = 3
# Output:
# 011011 001001 011101 010001 101011 111111
# 110011 101101 100001 110101 001010 011110
# 010010 001100 000000 010100 101110 100010
# 110110 100100

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        big = arr[-1]
        small = arr[0]
        ans = big - small

        small = arr[0] + k
        big = arr[n - 1] - k

        if small > big:
            small, big = big, small

            # Traverse middle elements
        for i in range(1, n - 1):

            subtract = arr[i] - k
            add = arr[i] + k

            # If both subtraction and addition
            # do not change diff
            if subtract >= small or add <= big:
                continue

            # Either subtraction causes a smaller
            # number or addition causes a greater
            # number. Update small or big using
            # greedy approach (If big - subtract
            # causes smaller diff, update small
            # Else update big)
            if big - subtract <= add - small:
                small = subtract
            else:
                big = add

        return min(ans, big - small)
