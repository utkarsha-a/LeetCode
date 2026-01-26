class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r//3)*3 + (c//3)
                    boxes[box_idx].add(val)

        def backtrack(idx):
            if idx==len(empty):
                return True
            r, c = empty[idx]
            box_idx = (r//3)*3 + (c//3)
            
            for num in map(str, range(1,10)):
                if num in rows[r] or num in cols[c] or num in boxes[box_idx]:
                    continue
                
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)

                if backtrack(idx+1):
                    return True
                
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_idx].remove(num)

            return False
        
        backtrack(0)
