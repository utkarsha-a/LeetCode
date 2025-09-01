class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hash = {}
        for n in nums:
            hash[n] = hash.get(n,0)+1

        for n in nums:
            if hash[n] == 1:
                return n        