class Solution:
    def isBipartite(self, n, graph):
        # code here

        def dfs(pos):

            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False

                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False

            return True

        color = {}

        for i in range(n):
            if i not in color:
                color[i] = 0

                if not dfs(i):
                    return 0

        return 1


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = 1
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(V, adj)
        if (ans):
            print("1")
        else:
            print("0")
