class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.append(0)
        m = len(cuts)
        cuts.sort()
        dp = [[-1]*(m+1) for _ in range(m+1)]

        def f(i, j):
            if i>j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            mini = float('inf')
            for idx in range(i, j+1):
                cost = cuts[j+1]-cuts[i-1] + f(i, idx-1) + f(idx+1, j)
                mini = min(mini, cost)
            dp[i][j] = mini
            return dp[i][j]
        
        return f(1,m-2)

        #memoization
        #O(m^3)
        #O(m^2)

        