class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if self.countDigits(i) % 2 == 0:
                count += 1
        return count

    def countDigits(self,x):
        digits = 0
        while x>0:
            x//=10
            digits += 1
        return digits
        