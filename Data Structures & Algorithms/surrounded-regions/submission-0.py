class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        df = [[0,1],[0,-1], [1,0],[-1,0]]
        visited = set()
        def dfs(i, j):
            board[i][j] = "A"
            for di, dj in df:
                ni, nj = i + di, j + dj
                if min(ni, nj) < 0 or ni >= ROW or nj >= COL or (ni, nj) in visited or board[ni][nj] != "O":
                    continue
                visited.add((ni,nj))
                dfs(ni, nj)
        for i in range(ROW):
            if board[i][0] == 'O' and (i,0) not in visited:
                dfs(i, 0)
            if board[i][COL-1] == 'O' and (i,COL-1) not in visited:
                dfs(i, COL-1)
        for j in range(COL):
            if board[0][j] == 'O' and (0,j) not in visited:
                dfs(0, j)
            if board[ROW-1][j] == 'O' and (ROW-1,j) not in visited:
                dfs(ROW-1, j)
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == 'O':
                    board[i][j] = 'X'