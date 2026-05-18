class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROW, COL = len(heights), len(heights[0])
        for i in range(ROW):
            pac.add((i, 0))
            atl.add((i, COL - 1))
        for j in range(COL):
            pac.add((0, j))
            atl.add((ROW - 1, j))
        def findSet(s):
            q = deque(s)
            df = [[0,1],[0,-1],[1,0],[-1,0]]
            while q:
                [i, j] = q.popleft()
                val = heights[i][j]
                for di, dj in df:
                    ni, nj = i + di, j + dj
                    if min(ni, nj) < 0 or ni >= ROW or nj >= COL or (ni, nj) in s or heights[ni][nj] < val:
                        continue
                    s.add((ni, nj))
                    q.append([ni, nj])
        findSet(pac)
        findSet(atl)
        ans = list(pac.intersection(atl))
        return ans