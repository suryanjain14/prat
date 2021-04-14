class cell:

    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


class Solution:
    def minStepToReachTarget(self, KnightPos, target, N):
        # Code here
        visited = [[0] * (N + 1)] * (N + 1)
        q = [(KnightPos[0], KnightPos[1])]

        while len(q) != 0:
            x, y = q.pop(0)

            if x - 2 < 1 or y - 1 < 1 or x - 2 > N or y - 1 > N or visited[x - 2][y - 1] > 0:
                visited[x - 2][y - 1] = visited[x][y] + 1
                q.append((x - 2, y - 1))

            if x - 2 < 1 or y + 1 < 1 or x - 2 > N or y + 1 > N or visited[x - 2][y + 1] > 0:
                visited[x - 2][y + 1] = 1 + visited[x][y]
                q.append((x - 2, y + 1))

            if x - 1 < 1 or y - 1 < 1 or x - 1 > N or y - 2 > N or visited[x - 1][y - 2] > 0:
                visited[x - 1][y - 2] = 1 + visited[x][y]
                q.append((x - 1, y - 2))

            if x - 1 < 1 or y + 2 < 1 or x - 1 > N or y + 1 > N or visited[x - 1][y + 1] > 0:
                visited[x - 1][y + 2] = 1 + visited[x][y]
                q.append((x - 1, y + 2))

            if x + 2 < 1 or y - 1 < 1 or x + 2 > N or y - 1 > N or visited[x + 2][y - 1] > 0:
                visited[x + 2][y - 1] = 1 + visited[x][y]
                q.append((x + 2, y - 1))

            if x + 2 < 1 or y + 1 < 1 or x + 2 > N or y + 1 > N or visited[x + 2][y + 1] > 0:
                visited[x + 2][y + 1] = 1 + visited[x][y]
                q.append((x + 2, y + 1))

            if x + 1 < 1 or y - 2 < 1 or x + 1 > N or y - 2 > N or visited[x + 1][y - 2] > 0:
                visited[x + 1][y - 2] = 1 + visited[x][y]
                q.append((x + 1, y - 2))

            if x + 1 < 1 or y + 2 < 1 or x + 1 > N or y + 2 > N or visited[x + 1][y + 2] > 0:
                print(x + 1, y + 2)
                visited[x + 1][y + 2] = 1 + visited[x][y]
                q.append((x + 1, y + 2,))

        return visited[target[0]][target[1]]


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        KnightPos = list(map(int, input().split(' ')))
        TargetPos = list(map(int, input().split(' ')))
        obj = Solution()
        ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
        print(ans)

# } Driver Code Ends
