class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

        #O(n^2)
        #O(n)
        '''

        #Optimized Solution: using binary search
        res = []

        def binary_search(res, n):
            l = 0
            r = len(res)-1
            while l<=r:
                m = (l+r)//2
                if res[m] == n:
                    return m
                elif res[m]>n:
                    r = m-1
                else:
                    l = m+1
            return l


        for n in nums:
            if not res or n>res[-1]:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n
        return len(res)

        #O(nlogn)
        #O(n)


