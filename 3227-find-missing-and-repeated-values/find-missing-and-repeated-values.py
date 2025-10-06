class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nsq = n*n

        expected = nsq*(nsq+1)//2
        expectedsq = nsq*(nsq+1)*(2*nsq+1)//6

        actual = 0
        actualsq = 0

        for i in range(n):
            for j in range(n):
                actual += grid[i][j]
                actualsq += grid[i][j]*grid[i][j]

        diff = actual-expected

        diffsq = actualsq-expectedsq

        summ = diffsq//diff

        a = (summ+diff)//2
        b = (summ-diff)//2

        return [a, b]