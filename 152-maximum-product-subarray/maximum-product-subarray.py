class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmax = curmin = 1

        for n in nums:
            temp = curmax*n
            curmax = max(temp, curmin*n, n)
            curmin = min(temp,curmin*n, n)
            res = max(res, curmax)

        return res

        #O(n)
        #O(1)