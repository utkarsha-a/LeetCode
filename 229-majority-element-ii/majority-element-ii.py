class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = {}
        l = []

        for num in nums:
            hash[num] = hash.get(num, 0)+1

        t = len(nums)//3

        for num, count in hash.items():
            if count>t:
                l.append(num)

        return l
