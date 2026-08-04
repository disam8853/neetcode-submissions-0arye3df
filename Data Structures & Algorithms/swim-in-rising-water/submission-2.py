class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        hq = [[grid[0][0], 0, 0]] #[curTime, i, j]
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        while hq:
            d, i, j = heapq.heappop(hq)
            curNum = grid[i][j]
            if d > dist[i][j]:
                continue
            for di, dj in dirs:
                ni,nj = i+di, j+dj
                if min(ni,nj) < 0 or ni >= m or nj >= n:
                    continue
                newDist = 0
                num = grid[ni][nj]
                if max(num, curNum) <= d:
                    newDist = d
                else:
                    newDist = num
                if newDist < dist[ni][nj]:
                    dist[ni][nj] = newDist
                    heapq.heappush(hq, [newDist, ni, nj])
        return dist[m-1][n-1]