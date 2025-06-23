class Solution:
    def findGCD(self, nums: List[int]) -> int:
        '''
        a = min(nums)
        b = max(nums)
        while a != 0:
            temp = b%a
            b = a
            a = temp

        return b
        '''
        a = min(nums)
        b = max(nums)
        while a!=0:
            a, b = b%a, a
        return b

        