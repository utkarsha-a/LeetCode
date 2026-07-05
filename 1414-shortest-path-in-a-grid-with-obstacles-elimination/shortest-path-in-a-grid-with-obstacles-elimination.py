class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque() 
        queue.append((0, 0, k, 0))  #[row, col, obstacles, steps]
        seen = set()
        seen.add((0, 0, k))
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            x, y, obs, steps = queue.popleft()

            if (x, y) == (m-1, n-1):
                return steps
            
            for dx, dy in dirs:
                newx, newy = x+dx, y+dy

                if 0<=newx<m and 0<=newy<n:
                    new_obs = obs-grid[newx][newy]

                    if new_obs>= 0 and (newx, newy, new_obs) not in seen:
                        seen.add((newx, newy, new_obs))
                        queue.append((newx, newy, new_obs, steps+1))
        
        return -1