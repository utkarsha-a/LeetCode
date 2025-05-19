class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n >= 5:
            n //= 5
            ans += n
        return ans
             
        '''
        time limit exceeded
        ans = 0
        for i in range(1, n+1):
            temp = i
            while temp%5 == 0:
                ans += 1
                temp//5
        return ans
        '''


        