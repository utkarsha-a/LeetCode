class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmp = {}
        for i in range(len(nums)):
            if target-nums[i] in hashmp:
                return [i, hashmp[target-nums[i]]]
            hashmp[nums[i]] = i
        return False



'''

        mp = {}
        for i in range(len(nums)):
            if target-nums[i] in mp:
                return [i, mp[target-nums[i]]]
            mp[nums[i]] = i
        
        return False
'''