def left(root):
    ans = []
    if root is None:
        return ans
    while root is not None:
        ans.append(root.data)
        root = root.left
    return ans[:-1]


def right(root):
    ans = []
    if root is None or root.right is None:
        return ans
    while root is not None:
        ans.append(root.data)
        root = root.right
    if len(ans) <= 2:
        return []
    ans.pop(0)
    ans.pop(-1)
    return ans[::-1]


def bottom(root):
    ans = []

    def helper(root):
        nonlocal ans
        if root:
            helper(root.left)
            ans.append(root.data)
            helper(root.right)

    return ans


def printBoundaryView(root):
    # Code here
    l = left(root)
    r = right(root)
    b = bottom(root)
    l.extend(b)
    l.extend(r)
    return l
