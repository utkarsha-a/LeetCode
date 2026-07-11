class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxx, premin = -1, nums[0]

        for i in range(1, n):
            if nums[i]>premin:
                maxx = max(maxx, nums[i]-premin)
            else:
                premin = nums[i]
        return maxx