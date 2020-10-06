
# 1

def recursionsort(array):
    def helper(array):
        if len(array) == 1:
            return array
        temp = helper(array[:-1])
        return st(temp, array[-1])

    return helper(array)


def st(array, element):
    if len(array) == 0:
        return [element]
    if array[-1] <= element:
        array.append(element)
        return array
    else:
        temp = st(array[:-1], element)
        temp.append(array[-1])
        return temp


# a = recursionsort([5,1,0,2,-3,-4,-9])
# print(a)

# 2

def stackrecursionsort(stack: list):
    def helper(Stack: list):
        if len(Stack) == 1:
            return Stack
        lastelemet = Stack.pop()
        sortedstack = helper(Stack)
        return ststack(sortedstack, lastelemet)

    return helper(stack)


def ststack(stack: list, element):
    if len(stack) == 0:
        return [element]
    if stack[-1] <= element:
        stack.append(element)
        return stack
    else:
        lastelement = stack.pop()
        temp = ststack(stack, element)
        temp.append(lastelement)
        return temp


# print(stackrecursionsort([5, 1, 0, 2, -3, -4, -9]))


# 3

def stackreverserecursion(stack):

    def helper(Stack :list):
        if len(Stack)==1:
            return Stack
        element=Stack.pop()
        stack=helper(Stack)
        return revhelper(stack,element)

    return helper(stack)


def revhelper(stack,element):
    if len (stack)==0:
        stack.append(element)
        return stack
    else:
        temp=stack.pop()
        stack=revhelper(stack,element)
        stack.append(temp)
        return stack



# print(stackreverserecursion([5, 1, 0, 2, -3, -4, -9]))


