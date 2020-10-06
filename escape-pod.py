def bfs(matrix, src, des):
    visited = [-1 for i in range(len(matrix))]
    visited[src] = src
    queue = [src]
    while len(queue) > 0:
        sp = queue.pop(0)
        for i in range(len(matrix)):
            if (matrix[sp][i][1] - matrix[sp][i][0]) != 0 and visited[i] == -1:
                if i == des:
                    visited[des] = sp
                    path = [des]
                    temp = des
                    while temp != src:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
                    temp = 1
                    total = float("inf")
                    crt = src
                    while temp != len(path):
                        entry = matrix[crt][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        total = min(total, diff)
                        crt = path[temp]
                        temp += 1
                    temp = 1
                    crt = src
                    while temp != len(path):
                        entry = matrix[crt][path[temp]]
                        if entry[1] < 0:
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = matrix[path[temp]][crt]
                        if entry[1] <= 0:
                            entry[1] -= total
                        else:
                            entry[0] += total
                        crt = path[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = sp
                    queue.append(i)
    return False


def binarySearch(array, target):
    # Write your code here.
    low = 0
    high = len(array) - 1
    if len(array) == 1:
        if target == array[0]:
            return 0
    while low < high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid
        elif target > array[mid]:
            low = mid
        print(mid)
        print(f'low :{low}')
        print(f'high :{high}')
    return -1


print(binarySearch([0, 1,73],73 ))
