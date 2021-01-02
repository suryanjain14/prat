# Subset Sum Problem | DP-25
#
# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# Example:
#
# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output: True
# There is a subset (4, 5) with sum 9.
#
# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
# Output: False
# There is no subset that add up to 30.

# check for
# Input: set[] = [ 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46 ] , sum = 284
# Output: True

class sss:


    def __init__(self):
        self.cache=list()
    def targetsubsetsum(self,array, target):


        # def helper(array, sum):
        #     if len(array) <= 0 or sum <= 0:
        #         return 0
        #     if dp[len(array) - 1] > 0:
        #         return dp[len(array) - 1]
        #     else:
        #         if array[-1] <= sum:
        #             print(dp,array,sum,"fr")
        #             dp[len(array) - 1] = max(helper(array[:-1], sum - array[-1]) + array[-1], helper(array[:-1], sum))
        #             print(dp, array)
        #         else:
        #             dp[len(array) - 1] = helper(array[:-1], sum)
        #         return dp[len(array) - 1]
        #
        # ans = helper(array, target)
        # print(ans,dp)
        # return ans == target
        self.cache = [[None] * (len(array) + 1)] * (target + 1)

        # def helper(ar, sum):
        #
        #
        #     if sum == 0:
        #         self.cache[sum][len(ar)] = True
        #         return True
        #     elif len(ar) == 0:
        #         self.cache[sum][len(ar)] = False
        #         return False
        #     if self.cache[sum][len(ar)] is not None:
        #         return self.cache[sum][len(ar)]
        #     if ar[-1] > sum:
        #         self.cache[sum][len(ar)] = helper(ar[:-1], sum)
        #     else:
        #         self.cache[sum][len(ar)] = helper(ar[:-1], sum - ar[-1]) or helper(ar[:-1], sum)
        #     return self.cache[sum][len(ar)]

        def helper(array, sum):
            n = len(array)
            dp = [[False] * (sum + 1)] * (n + 1)

            for i in range(0, n + 1):
                for j in range(0, sum + 1):
                    if i == 0:
                        dp[i][j] = False
                    if j == 0:
                        dp[i][j] = True

            for i in range(1, n + 1):
                for j in range(1, sum + 1):
                    if j >= array[i - 1]:
                        dp[i][j] = dp[i - 1][j - array[i - 1]] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
            for x in dp:
                print(x)
            return dp[-1][-1]

        return helper(array, target)

obj= sss()
print(obj.targetsubsetsum([3, 34, 4, 12, 5, 2], 13))

# [39, 80, 91, 58, 59, 92, 16, 89, 57, 12, 3, 35, 73, 56, 29, 47, 63, 87, 76, 34, 70, 43, 45, 17, 82, 99, 23, 52, 22,
#  100, 58, 77, 93, 90, 76, 13, 1, 11, 4, 70, 62, 89, 2, 90, 56, 24, 3, 86, 83, 86, 89, 27, 18, 58, 33, 33, 70, 55,
    #  22, 90, 77, 30], 2369)
