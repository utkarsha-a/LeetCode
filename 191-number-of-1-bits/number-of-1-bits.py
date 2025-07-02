class Solution:
    def hammingWeight(self, n: int) -> int:
        res = bin(n).count('1')
        return res
        