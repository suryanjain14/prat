# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=None,right=None,left=None):
        self.key = value
        self.right = right
        self.left = left

    def insert(self, key):
        if self.key is None:
            self.key=key
            return
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)
        else:  # self.value > value
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


from copy import copy

def generateTree(n):
    ans=[]
    n=list(range(1,n+1))
    cache = {}
    node = TreeNode()
    def helper(output,n,treelist):
        nonlocal ans
        nonlocal cache
        if len(n)==0:
            if str(treelist) in cache:
                return
            cache[str(treelist)]=True
            ans.append(output)
            return
        for i in range(0,len(n)):
            remaning = n[:i]+n[i+1:]

    helper(node,n,[])




