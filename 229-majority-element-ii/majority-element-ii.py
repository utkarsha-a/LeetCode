class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = {}
        l = []
        for n in nums:
            hash[n] = hash.get(n, 0)+1
            if hash[n]>len(nums)//3:
                if n not in l:
                    l.append(n)
        return l