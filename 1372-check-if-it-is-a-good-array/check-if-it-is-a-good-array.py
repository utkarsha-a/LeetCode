class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        current_gcd = nums[0]
        for i in nums:
            current_gcd = gcd(current_gcd,i)
        return current_gcd == 1
        