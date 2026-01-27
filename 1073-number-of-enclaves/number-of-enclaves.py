class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def capture(r, c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            if grid[r][c] != 1:
                return

            grid[r][c] = 2
            capture(r, c+1)
            capture(r, c-1)
            capture(r+1, c)
            capture(r-1, c)

        for i in range(rows):
            capture(i, 0)
            capture(i, cols-1)
        for j in range(cols):
            capture(0, j)
            capture(rows-1, j)

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt += 1
                
        return cnt
        