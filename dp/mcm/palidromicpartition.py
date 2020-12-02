def palindromicPartition(string):
    # code here
    def solve(st, i, j):
        if i >= j or st == st[::-1]:
            return 0
        ans = float("inf")
        for k in range(i, j):
            temp_ans = solve(st[i:k + 1], i, k) + solve(st[k:j + 1], k + 1, j) + 1
            ans = min(ans, temp_ans)
        return ans

    return solve(string, 0, len(string) - 1)


print(palindromicPartition("ababbbabbababa"))
