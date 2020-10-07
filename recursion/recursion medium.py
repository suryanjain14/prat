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
    return ans


# print( subsets('abc'))
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


print(permutations([1,2,3,4]))


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


