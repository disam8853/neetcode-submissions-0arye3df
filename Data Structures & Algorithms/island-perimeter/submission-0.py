class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        diff = [[0,1], [0,-1],[1,0],[-1,0]]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                ans += 4
                for di, dj in diff:
                    ni, nj = i + di, j + dj
                    if min(ni, nj) < 0 or ni >= m or nj >= n:
                        continue
                    if grid[ni][nj] == 1:
                        ans -= 1
        return ans