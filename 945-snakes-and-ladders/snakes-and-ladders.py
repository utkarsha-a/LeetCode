class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells: List[int] = [-1]  
        ltr = True  
        for r in range(n - 1, -1, -1):  
            row = board[r] if ltr else list(reversed(board[r]))
            cells.extend(row)
            ltr = not ltr
        target = len(cells) - 1  

        queue = deque([(1, 0)]) 
        visited = {1}

        while queue:
            square, moves = queue.popleft()

            if square == target:
                return moves

            if square >= target - 6:
                return moves + 1

            jump_mask = []
            for r in range(1, 7):
                if square + r <= target:
                    jump_mask.append(cells[square + r] != -1)
                else:
                    jump_mask.append(False)
                    
            deepest_plain = None
            for r in range(6, 0, -1):  
                landing = square + r
                if landing > target:
                    continue
                    
                if jump_mask[r - 1]:  
                    dest = cells[landing]
                    if dest == target: 
                        return moves + 1
                    if dest not in visited:
                        visited.add(dest)
                        queue.append((dest, moves + 1))
                else:  
                    if landing not in visited:
                        visited.add(landing) 
                        if deepest_plain is None:
                            deepest_plain = landing  
                            
            if deepest_plain is not None:
                queue.append((deepest_plain, moves + 1))
                
        return -1  
        