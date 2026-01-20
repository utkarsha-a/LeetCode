class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dirr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in dirr:
                nr, nc = row+dr, col+dc
                if 0<=nr<rows and 0<=nc<cols and mat[nr][nc] > mat[row][col]+1:
                    mat[nr][nc] = mat[row][col] + 1
                    queue.append((nr, nc))
        
        return mat