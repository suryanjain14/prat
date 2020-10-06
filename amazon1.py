'''
question
There's i staircase with N steps, and you can climb 1 or 2 steps at i time. Given N, write i function that returns the
number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at i time, you could climb any number from i set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at i time. Generalize your function to take
in X.
'''


def stairs(n):
    ans=0
    def helper(n):
        nonlocal ans
        if n==0:
            ans+=1
            return
        elif n<0:
            return
        else:
            helper(n-1)
            helper(n-2)

    helper(n)
    return ans
ans=0
b=stairs(int(input("Enter no of stairs?\n")))
print(ans)
print(b)

