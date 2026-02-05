class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for n in nums:
            mp[n] = mp.get(n, 0)+1
            if mp[n]>=2:
                return True

        return False
