class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        shortest = float('inf')
        summ = 0
        if sum(nums)<target:
            return 0

        for r in range(len(nums)):
            summ += nums[r]
            if summ<target:
                continue

            while summ>=target:
                shortest = min(shortest, r-l+1)
                summ -= nums[l]
                l += 1

        return shortest

        