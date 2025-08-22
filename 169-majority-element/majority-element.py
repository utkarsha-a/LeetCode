class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maj = 0
        for n in nums:
            if maj==0:
                res =n
            if n==res:
                maj+=1
            else:
                maj-=1
        return res
        