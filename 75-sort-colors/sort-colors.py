class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0)+1
        
        idx = 0

        for n in range(3):
            freq = count.get(n,0)
            nums[idx:idx+freq] = [n]*freq
            idx += freq
