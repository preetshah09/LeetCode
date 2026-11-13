class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix) #getting length of Row
        cols = len(matrix[0]) #getting length of Column

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols
            val = matrix[row][col]

            if matrix[row][col] == target:
                return True
            elif  matrix[row][col] < target:
                low = mid + 1 # if I write mid=low+1 it will show Time Limit Excede Error
            else:
                high = mid - 1
        return False
