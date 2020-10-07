def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    memo = [-1] * len(items)

    def helper(items, capacity, memo):
        if len(items) == 0 or capacity == 0:
            return 0
        if memo[len(items) - 1] != -1:
            return memo[len(items) - 1]
        if items[-1][1] <= capacity:
            memo[len(items) - 1] = max(items[-1][0] + helper(items[:-1], capacity - items[-1][1], memo),
                                       helper(items[:-1], capacity, memo))
        elif items[-1][1] > capacity:
            memo[len(items) - 1] = helper(items[:-1], capacity, memo)
        return memo[len(items) - 1]

    ans = helper(items, capacity, memo)

    return ans
