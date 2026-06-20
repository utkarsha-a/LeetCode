class Solution:
    def countBits(self, n: int) -> List[int]:
        #DP SOLUTION - O(n)
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        
        return dp
        
        '''
        O(nlogn)
        ans = [0] * (n+1)
        for i in range(1, n+1):
            num = i
            res = 0
            while num!=0:
                res += 1
                num = num & (num-1)
            ans[i] = res
        return ans
        '''