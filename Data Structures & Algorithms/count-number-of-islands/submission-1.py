class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        ROW = len(grid)
        COL = len(grid[0])
        ans = 0
        def dfs(i, j):
            grid[i][j] = '2'

            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or grid[nr][nc] != '1':
                    continue
                dfs(nr, nc)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans