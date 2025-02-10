class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)
        return nums[i//2]

        