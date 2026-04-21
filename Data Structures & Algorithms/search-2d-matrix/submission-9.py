class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        bot, top = 0, ROWS - 1

        while bot <= top:
            midRow = (top + bot) // 2
            if target > matrix[midRow][-1]:
                bot = midRow + 1
            elif target < matrix[midRow][0]:
                top = midRow - 1
            else:
                break
            
        if not (bot <= top):
            return False
        
        midRow = (top + bot) // 2
        l, r = 0, COLS - 1
        while l<=r:
            m = (l+r) //2
            if target > matrix[midRow][m]:
                l = m+1
            elif target < matrix[midRow][m]:
                r = m-1
            else:
                return True
        return False