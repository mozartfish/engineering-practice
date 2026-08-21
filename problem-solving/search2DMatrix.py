from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        lo = 0
        hi = ROWS * COLS - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            r = mid // COLS
            c = mid % COLS

            if target == matrix[r][c]:
                return True
            if target > matrix[r][c]:
                lo = mid + 1
            if target < matrix[r][c]:
                hi = mid - 1

        return False
