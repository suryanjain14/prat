# inputoutputmethod


# programm to return all the subsets of a string

def subsets(string):
    ans = []

    def helper(output, string, ans):
        if len(string) == 0:
            ans.append(output)
            return
        helper(output, string[1:], ans)
        helper(output + string[0], string[1:], ans)

    helper('', string, ans)
    return sorted(ans)


print( subsets('abc'))
#
def permutations(nums):
    ans = []

    def helper(output, nums, ans):
        if len(nums) == 0:
            ans.append(output)
            return
        else:
            for i in range(0, len(nums)):
                remaning = nums[:i] + nums[i + 1:]
                helper(output + [nums[i]], remaning, ans)

    helper([], nums, ans)
    return ans


# print(permutations([1, 2, 3, 4]))


def permuteUnique(nums):
    ans = []
    unique = {}

    def helper(output, st, nums, ans, unique):
        if len(nums) == 0:
            if st in unique:
                return
            ans.append(output)
            unique[st] = st
            return
        else:
            for i in range(0, len(nums)):
                remaning = nums[:i] + nums[i + 1:]
                helper(output + [nums[i]], st + f"a{nums[i]}aa", remaning, ans, unique)

    helper([], "", nums, ans, unique)

    return ans

    # print(permuteUnique([1, 1, 2]))


def balenceparenthesis(no):
    ans = []

    def helper(string, o, c, array):
        if o == 0 and c == 0:
            array.append(string)
            return

        if o < c and o > 0:
            helper(string + '(', o - 1, c, array)
            helper(string + ")", o, c - 1, array)
        elif o == 0:
            helper(string + ")", o, c - 1, array)
        elif c == o:
            helper(string + "(", o - 1, c, array)

    helper('', no, no, ans)
    return ans


# print(balenceparenthesis(3))


# Print all possible strings of length k that can be formed from a set of n characters
# Examples:
#
# Input:
# set[] = {'a', 'b'}, k = 3
#
# Output:
# aaa
# aab
# aba
# abb
# baa
# bab
# bba
# bbb
#
#
# Input:
# set[] = {'a', 'b', 'c', 'd'}, k = 1
# Output:
# a
# b
# c
# d
# For a given set of size n, there will be n^k possible strings of length k. The idea is to start from an empty output string (we call it prefix in following code). One by one add all characters to prefix. For every character added, print all possible strings with current prefix by recursively calling for k equals to k-1.
# Below is the implementation of above idea :

def allpossiblestring(set=[], k=0):
    def helper(string, k):
        nonlocal set
        if k == 0:
            print(string)
        else:
            for i in set:
                helper(string + i, k - 1)
        return

    helper("", k)


allpossiblestring(["a", "b","c"], k=2)
