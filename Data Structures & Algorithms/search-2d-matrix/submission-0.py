class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for col in matrix:
            for row in col:
                print(row)
                if target == row:
                    return True
                
        return False






        """for col in range(len(matrix)):
            row = len(col)
            for row in range(len(col)):
                if row == target:
                    return true
                else:
                    return false"""
