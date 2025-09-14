class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxl = 1
        n = len(nums)
        curl = 1
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                curl += 1
                maxl = max(maxl, curl)
                
            else:
                curl = 1
        return maxl
        