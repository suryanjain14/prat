# Que) Largest Rectangular Area in a Histogram |SET2
# Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of
# contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.
# For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}.
# The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)


def histogramArea(array: list):
    right=nsr(array)
    left=nsl(array)
    ans=0
    for i in range(0, len(right)):
        width=right[i] - left[i] - 1
        ans=max(width*array[i],ans)
    return ans



def nsl(array):
    stack=[]
    left=[]
    for index in range(0,len(array)):

        if len(stack) == 0:
            left.append(index-1)
        elif array[stack[-1]] <= array[index]:
            left.append(stack[-1])
        elif array[stack[-1]] > array[index]:
            while len(stack) > 0 and array[stack[-1]] > array[index]:
                stack.pop()
            if len(stack) == 0:
                left.append(index-1)
            else:
                left.append(stack[-1])
        stack.append(index)
    return left

def nsr(array):
    stack=[]
    right=[]
    for index in range(len(array)-1,-1,-1):
        if len(stack)==0:
            right.append(index+1)
        elif array[stack[-1]]<=array[index]:
            right.append(stack[-1])
        elif array[stack[-1]]>array[index]:
            while len(stack) > 0 and array[stack[-1]]>array[index]:
                stack.pop()
            if len(stack) == 0:
                right.append(index+1)
            else:
                right.append(stack[-1])
        stack.append(index)
    return right[::-1]
#


print(histogramArea([6, 2, 5, 4, 5, 1, 6]))