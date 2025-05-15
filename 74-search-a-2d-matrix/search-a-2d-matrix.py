class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c= len(matrix[0])
        l = 0
        rig = r*c-1

        while l<=rig:
            mid = (l+rig)//2
            row, col = mid//c, mid % c
            guess = matrix[row][col]

            if guess == target:
                return True
            elif guess < target:
                l = mid+1
            else: 
                rig = mid-1

        return False