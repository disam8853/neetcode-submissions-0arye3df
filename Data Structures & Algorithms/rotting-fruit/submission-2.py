class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        lvl = -1
        ROW, COL = len(grid), len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append([i, j])
        df = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            for _ in range(len(q)):
                [i,j] = q.popleft()
                for di, dj in df:
                    ni, nj = i + di, j + dj
                    if min(ni, nj) < 0 or ni >= ROW or nj >= COL or grid[ni][nj] != 1:
                        continue
                    grid[ni][nj] = 2
                    q.append([ni, nj])
            lvl += 1
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        return lvl if lvl >= 0 else 0
