class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                bi = (i//3)*3 + (j//3)
                if num in r[i] or num in c[j] or num in b[bi]:
                    return False
                r[i].add(num)
                c[j].add(num)
                b[bi].add(num) 
        return True      