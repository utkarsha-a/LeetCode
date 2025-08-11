class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aboveR = [1]*n
        for _ in range(m-1):
            currR = [1]*n
            for i in range(1,n):
                currR[i] = currR[i-1] + aboveR[i]
            aboveR = currR

        return aboveR[-1]