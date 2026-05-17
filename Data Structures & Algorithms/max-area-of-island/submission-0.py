class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        ROW, COL = len(grid), len(grid[0])
        df = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i, j):
            if min(i, j) < 0 or i >= ROW or j >= COL or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            rtn = 1
            for di, dj in df:
                ni, nj = i + di, j + dj
                rtn += dfs(ni, nj)
            return rtn
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans