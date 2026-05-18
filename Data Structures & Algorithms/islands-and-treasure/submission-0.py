class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        ROW, COL = len(grid), len(grid[0])
        df = [[0,1], [0,-1], [1,0], [-1,0]]
        def findDistance(i, j):
            q = deque([[i, j]])
            dis = 0
            while q:
                for _ in range(len(q)):
                    [i, j] = q.popleft()
                    grid[i][j] = min(grid[i][j], dis)
                    for di, dj in df:
                        ni, nj = i + di, j + dj
                        if min(ni, nj) < 0 or ni >= ROW or nj >= COL or grid[ni][nj] < dis + 1:
                            continue
                        q.append([ni, nj])
                dis += 1
                
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    findDistance(i, j)