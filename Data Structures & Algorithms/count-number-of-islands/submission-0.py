class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        ans = 0
        df = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(i, j):
            if min(i,j) < 0 or i >= ROW or j >= COL or grid[i][j] != "1":
                return
            grid[i][j] = "2"

            for di, dj in df:
                ni, nj = i + di, j + dj
                dfs(ni, nj)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans