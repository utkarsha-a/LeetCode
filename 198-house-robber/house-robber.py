class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        maxx = 0

        for curr in nums:
            temp = max(maxx, prev + curr)
            prev = maxx
            maxx = temp
        
        return maxx