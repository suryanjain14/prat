def nSmallerRight(array):
    stack = []
    smaller_right = []
    for i in array[::-1]:
        if len(stack) == 0:
            smaller_right.append(float("inf"))
        elif stack[-1] <= i:
            smaller_right.append(stack[-1])
        elif stack[-1] > i:
            while len(stack) > 0 and stack[-1] > i:
                stack.pop()
            if len(stack) == 0:
                smaller_right.append(float("inf"))
            else:
                smaller_right.append(stack[-1])
        stack.append(i)

    return smaller_right[::-1]


def nSmallerLeft(array):
    stack = []
    smaller_left = []
    for i in array:
        if len(stack) == 0:
            smaller_left.append(float("inf"))
        elif stack[-1] <= i:
            smaller_left.append(stack[-1])
        elif stack[-1] > i:
            while len(stack) > 0 and stack[-1] > i:
                stack.pop()
            if len(stack) == 0:
                smaller_left.append(float("inf"))
            else:
                smaller_left.append(stack[-1])
        stack.append(i)

    return smaller_left


array = [1, 2, 0, 0, 4, 3, 2]
# ans= nSmallerRight(array)
ans = nSmallerLeft(array)
print(array)
print(ans)
