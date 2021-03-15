from bisect import bisect_right


class Solution:

    def median(self, matrix, r, c):
        # code here
        mn = float("inf")
        mx = float("-inf")
        for i in matrix:
            if i[0] < mn:
                mn = i[0]
            if i[-1] > mx:
                mx = i[-1]
        temp = (1 + (r * c)) // 2

        while mn < mx:

            mid = (mn + mx) // 2
            # print(mn, mx,mid)
            count = 0
            for i in matrix:
                count += bisect_right(i, mid)
            if count < temp:
                mn = mid + 1
            elif count >= temp:
                mx = mid
                # print("AS",mx,mid)
        return mn


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = 1
    for _ in range(t):
        r, c = (3, 3)
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in '1 3 5 2 6 9 3 6 9'.strip().split()]
        k = 0
        for i in range(r):
            for j in range(c):
                matrix[i][j] = line1[k]
                k += 1
        ans = ob.median(matrix, r, c);
        print(ans)
