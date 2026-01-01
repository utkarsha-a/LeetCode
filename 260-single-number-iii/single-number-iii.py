class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num
        
        p = 0
        while res%2==0:
            p += 1
            res /=2
        mask = 1<<p
        l = 0
        r = 0
        for num in nums:
            if num&mask==0:
                l ^=num
            else:
                r ^= num

        return [l, r]