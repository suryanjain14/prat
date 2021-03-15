class Solution:
    def lps(self, s):
        # code here
        n = len(s)
        cache = [0] * n
        ln = 0
        i = 1
        ans = 0
        while i < n:
            if s[i] == s[ln]:
                cache[i] = ln + 1
                ans = max(cache[i], ans)
                i += 1
                ln += 1
            else:
                if ln != 0:
                    ln = cache[ln - 1]
                else:
                    i += 1
        return ans


a = Solution()
z = a.lps("onionsonioons")
print(z)
