class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        startColour = image[sr][sc]
        
        if color == startColour:
            return image
        
        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or image[i][j] != startColour:
                return
            image[i][j] = color
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        dfs(sr, sc)
        return image