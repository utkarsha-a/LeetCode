class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        def binary_search(res,n):
            l = 0
            r = len(res)-1

            while l<=r:
                m = (l+r)//2
                if res[m]==n:
                    return m
                elif res[m]>n:
                    r = m-1
                else:
                    l = m+1
            return l

        for n in nums:
            if not res or res[-1]<n:
                res.append(n)
            else:
                idx = binary_search(res,n)
                res[idx] = n
        
        return len(res)
        