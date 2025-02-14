class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        n = len(nums)

        for i in range(n):
            hashMap[nums[i]] = i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]

        return []