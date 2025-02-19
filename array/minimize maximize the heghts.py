# Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each
# tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer.
# Find out what could be the possible minimum difference of the height of shortest and longest towers after you have
# modified each tower.
#
# Example 1:
#
# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output: 5
# Explanation: The array can be modified as
# {3, 3, 6, 8}. The difference between
# the largest and the smallest is 8-3 = 5.
#
# Example 2:
#
# Input:
# K = 3, N = 5
# Arr[] = {3, 9, 12, 16, 20}
# Output: 11
# Explanation: The array can be modified as
# {6, 12, 9, 13, 17}. The difference between
# the largest and the smallest is 17-6 = 11.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function getMinDiff() which takes the
# arr[], n and k as input parameters and returns an integer denoting the minimum difference.
#
#
# Expected Time Complexity: O(N*logN)
# Expected Auxiliary Space: O(N)
#
# Constraints
# 1 ≤ K ≤ 104
# 1 ≤ N ≤ 105
# 1 ≤ Arr[i] ≤ 105


class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        visited, possibleheights = [], []
        for i in range(n):
            if arr[i] - k >= 0:
                possibleheights.append([arr[i] - k, i])
            possibleheights.append([arr[i] + k, i])
            visited.append(0)
        possibleheights.sort()
        right = 0
        left = 0
        element = 0
        while element < n and right < len(possibleheights):
            if visited[possibleheights[right][1]] == 0:
                element += 1
            visited[possibleheights[right][1]] += 1
            right += 1
            ans = possibleheights[right - 1][0] - possibleheights[left][0]

        while right < len(possibleheights):

            if visited[possibleheights[left][1]] == 1:
                element -= 1
            visited[possibleheights[left][1]] -= 1
            left += 1
            while right < len(possibleheights) and element < n:
                if visited[possibleheights[right][1]] == 0:
                    element += 1
                visited[possibleheights[right][1]] += 1
                right += 1

            if element == n:
                ans = min(ans, possibleheights[right - 1][0] - possibleheights[left][0])
            else:
                break

        return ans
