class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for n in nums:
            if n==0:
                count = 0
            else:
                count+=1

            if res<count:
                res = count
        return res

        