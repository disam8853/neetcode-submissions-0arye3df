class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        rowCnt = [0] * ROW
        colCnt = [0] * COL
        st = set()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    rowCnt[i] += 1
                    colCnt[j] += 1
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in st or grid[i][j] != 1:
                    continue
                if rowCnt[i] > 1 or colCnt[j] > 1:
                    st.add((i,j))
        return len(st)