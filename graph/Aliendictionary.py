class Solution:
    def findOrder(self, dic, N, K):
        # code here
        if N == 1:
            return [i for i in dic[0]]
        graph = {}
        p1, p2 = 0, 1
        i = 0
        while p2 < N:
            w1 = dic[p1]
            w2 = dic[p2]
            if w1[0] == w2[0]:
                while w1[i] == w2[i] and i < len(w1):
                    i += 1
                if w1[i] != w2[i]:
                    if w2[i] in graph:
                        graph[w2[i]].add(w1[i])
                    else:
                        graph[w2[i]] = {w1[i]}
                    if w1[i] not in graph:
                        graph[w1[i]] = set()

                i = 0
            else:
                if w2[i] in graph:
                    graph[w2[i]].add(w1[i])
                else:
                    graph[w2[i]] = {w1[i]}
                if w1[i] not in graph:
                    graph[w1[i]] = set()

            p1 += 1
            p2 += 1
        print(graph)
        visited = {}
        stack = []

        def dfs(node):
            if node in visited:
                return
            nodes = graph[node]
            visited[node] = True
            for i in nodes:
                dfs(i)
            stack.append(node)

        for i in graph:
            dfs(i)
        return stack
        # return ['b','d','a','c']


# {
#  Driver Code Starts
# Initial Template for Python 3

class sort_by_order:
    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = 1
    for _ in range(t):

        n = 5
        k = 4

        alien_dict = [x for x in 'baa abcd abca cab cada'.strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)

        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)

        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)
