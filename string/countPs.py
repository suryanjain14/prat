def countPs(string):
    # Code here
    ans = []

    def helper(string, temp):
        nonlocal ans
        if len(string) == 0:
            return
        else:
            temp2 = temp + string[0]
            if temp2 == temp2[::-1]:
                ans.append(temp2)
            helper(string[1:], temp)
            helper(string[1:], temp2)
            return

    helper(string, '')
    print(ans)
    return len(ans)


print(countPs('abcd'))
