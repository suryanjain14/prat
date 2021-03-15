def sol(array):
    cache = {}
    ans = 0
    n = len(array)

    def swap(i, j):
        nonlocal array
        nonlocal cache
        for i in range(j, i + 1, -1):
            array[i], array[i - 1] = array[i - 1], array[i]
            if cache[array[i]] <= i:
                cache[array[i]] = i

    for i in range(n):
        if array[i] in cache:
            ans = ans + i - cache[array[i]] - 1
            temp = cache[array[i]]
            swap(cache[array[i]], i)
            cache[array[temp]] = temp + 1
        else:
            cache[array[i]] = i
        print(array, cache, ans, array[i], i)

    return ans


print(sol([2, 1, 1, 3, 1, 1, 1]))
