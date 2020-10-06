# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value,right=None,left=None):
        self.key = value
        self.right = None
        self.left = None

    def insert(self, key):
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


def printInorder( root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


class Solution:
    ans = []
    def __init__(self):
        pass

    def generateTrees(self, n: int):

        def helper(node, input, root):

            if len(input) == 0:
                print("input", input)
                print("Final Final Final")
                root.display()
                self.ans.append(root)
                return
            else:
                for index, i in enumerate(input):

                    if root is None:
                        print("input", input)
                        print("root")
                        print(i)
                        newnode = TreeNode(i)
                        helper(newnode, input[:index] + input[index + 1:], newnode)

                    else:
                        print("input", input)
                        if i > node.key:
                            print('in right')

                            newnode = TreeNode(i)
                            node.right = newnode
                        else:
                            newnode = TreeNode(i)
                            node.left = newnode
                            print('in left')

                        print(i)
                        print("Inter INter iNter")
                        root.display()
                        helper(newnode, input[:index] + input[index + 1:], root)
                return

        helper(None, list(range(1, n + 1)), None)





a = Solution()
a.generateTrees(3)
