# your code goes here

def isvalid(arr, c, n, mid):
    prev = arr[0]
    cow = 1
    for i in range(1, n):
        if arr[i] - prev >= mid:
            cow += 1
            prev = arr[i]
    if cow < c:
        return False
    return True


cases = int(input())
for _ in range(cases):
    n, c = list(map(int, input().strip().split()))
    arr = []
    res = -1
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    end, start = arr[-1], arr[0]
    while end >= start:
        mid = (end + start) // 2

        if isvalid(arr, c, n, mid):
            res = max(res, mid)
            start = mid + 1
        else:
            end = mid - 1

    print(res)
