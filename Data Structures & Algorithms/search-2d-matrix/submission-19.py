class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS, ROWS = 0, len(matrix)

        bot, top=0, ROWS-1

        while bot<=top:
            midRow = (bot+top)//2
            if matrix[midRow][-1] < target:
                bot = midRow + 1
            elif matrix[midRow][0] > target:
                top = midRow - 1
            else:
                break
        
        if not (bot<=top):
            return False

        midRow = (bot+top)//2
        l, r = 0, len(matrix[midRow])-1

        while l<=r:
            m = (l+r)//2
            if matrix[midRow][m] > target:
                r=m-1
            elif matrix[midRow][m] < target:
                l=m+1
            else:
                return True
        return False