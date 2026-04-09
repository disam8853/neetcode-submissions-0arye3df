class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowNum = len(matrix)
        colNum = len(matrix[0])
        def getIdx(idx):
            return [idx // colNum, idx % colNum]
        l = 0
        r = rowNum * colNum
        while l < r:
            mid = (l + r) // 2
            row, col = getIdx(mid)
            n = matrix[row][col]
            if n == target:
                return True
            elif n > target:
                r = mid
            elif n < target:
                l = mid + 1
        return False