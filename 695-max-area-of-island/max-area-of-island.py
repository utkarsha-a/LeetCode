class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if (0<=r<rows and 0<=c<cols and grid[r][c]==1 and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
