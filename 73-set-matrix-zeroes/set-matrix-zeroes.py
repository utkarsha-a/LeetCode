class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        frow = False
        fcol = False

        for i in range(rows):
            if matrix[i][0] == 0:
                fcol = True
            
        for j in range(cols):
            if matrix[0][j] == 0:
                frow =True
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix [0][j] = matrix[i][0] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        if fcol:
            for i in range(rows):
                matrix[i][0] = 0

        if frow:
            for j in range(cols):
                matrix[0][j] = 0