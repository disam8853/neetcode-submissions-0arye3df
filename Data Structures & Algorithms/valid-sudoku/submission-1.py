class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHm = [set() for _ in range(9)]
        colHm = [set() for _ in range(9)]
        squarHm = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if not '0' <= board[i][j] <= '9':
                    continue
                n = board[i][j]
                squarIdx = (i//3)*3 + j//3
                if n in rowHm[i] or n in colHm[j] or n in squarHm[squarIdx]:
                    return False
                rowHm[i].add(n)
                colHm[j].add(n)
                squarHm[squarIdx].add(n)

        return True