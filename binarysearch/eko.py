# n,m = 4,8
# arr = [20,10,15,17]

n, m = 5, 20
arr = [4, 42, 40, 26, 46]


# n, m = list(map(int, input().strip().split(' ')))
# arr = list(map(int, input().strip().split(' ')))


def isvalid(arr, m, mid):
    sm = 0
    for i in arr:
        if i >= mid:
            sm = sm + i - mid
    if sm >= m:
        return True
    return False


start, end = 0, max(arr)
res = 0

while start <= end:
    mid = (start + end) // 2
    if isvalid(arr, m, mid):
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
