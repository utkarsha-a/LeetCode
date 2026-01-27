class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n:
                return
            if grid[r][c] != 0:
                return 
            
            grid[r][c] = 2
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    cnt += 1
                    dfs(r, c)

        return cnt