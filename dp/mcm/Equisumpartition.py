# 416. Partition Equal Subset Sum
# Medium
#
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
#
#
# Example 1:
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

def equisumpartition(array):
    def helper(array, k):
        dp = [[None] * k] * len(array)
        for i in range(len(array) + 1):
            for j in range(k + 1):
                if i == 0:
                    dp[i][j] = False
                if k == 0:
                    dp[i][j] = True

        for i in range(len(array) + 1):
            for j in range(k + 1):
                if array[i] <= j:
                    dp[i][j] = dp[i - 1][j - array[i]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    return helper(array, sum(array) / 2) if sum(array) % 2 == 0 else False


print(helper)
