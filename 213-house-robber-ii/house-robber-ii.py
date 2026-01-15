class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxmoney(nums):
            prev = 0
            maxx = 0
            for cur in nums:
                temp = max(maxx, prev+cur)
                prev = maxx
                maxx = temp
            return maxx
        return max(maxmoney(nums[1:]), maxmoney(nums[:-1]), nums[0])
        