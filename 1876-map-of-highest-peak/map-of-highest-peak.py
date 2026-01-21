class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        dirr = [(0,1), (0, -1), (1, 0), (-1,0)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]==1:
                    queue.append((r, c))
                    isWater[r][c] = 0
                else:
                    isWater[r][c] = float('inf')
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in dirr:
                nr, nc = row+dr, col+dc
                if 0<=nr<rows and 0<=nc<cols and isWater[nr][nc] > isWater[row][col] + 1:
                    isWater[nr][nc] = isWater[row][col]+1
                    queue.append((nr,nc))
        
        return isWater
                
        