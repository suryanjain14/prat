# Next Greater Element
# Last Updated: 24-07-2019
# Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.
#
# Examples:
#
# For any array, rightmost element always has next greater element as -1.
# For an array which is sorted in decreasing order, all elements have next greater element as -1.
# For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.
# Element       NGE
#    4      -->   5
#    5      -->   25
#    2      -->   25
#    25     -->   -1
# d) For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows.
#
#   Element        NGE
#    13      -->    -1
#    7       -->     12
#    6       -->     12
#    12      -->     -1



def nGreaterRight(array):
    stack = [] #memo for right array
    greater_array = []
    for i in array[::-1]:
        if len(stack) == 0:
            greater_array.append(-1)
        elif i <= stack[-1]:
            greater_array.append(stack[-1])
        elif i > stack[-1]:
            while len(stack) > 0 and stack[-1] < i:
                stack.pop()
            if len(stack) == 0:
                greater_array.append(-1)
            else:
                greater_array.append(stack[-1])
        stack.append(i)
    return greater_array[::-1]

def nGreaterLeft(array):
    stack=[]
    greater_left=[]

    for i in array:
        if len(stack)==0:
            greater_left.append(-1)
        elif stack[-1]>=i:
            greater_left.append(stack[-1])
        elif stack[-1]<i:
            while len(stack)>0 and stack[-1]<i:
                stack.pop()
            if len(stack)==0:
                greater_left.append(-1)
            else:
                greater_left.append(stack[-1])
        stack.append(i)

    return greater_left





array=[1, 2, 0, 0, 4, 3, 2]
# ans = nGreaterRight(array)
ans = nGreaterLeft(array)
print(array)
print(ans)