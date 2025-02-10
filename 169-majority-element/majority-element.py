class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num1 = nums.sort()
        i = len(nums)//2
        m = nums[i]
        return m

        