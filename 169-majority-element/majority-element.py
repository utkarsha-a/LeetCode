class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for num in nums:
            hash[num] = hash.get(num,0)+1
            if hash[num] > len(nums) // 2:
                return num
        