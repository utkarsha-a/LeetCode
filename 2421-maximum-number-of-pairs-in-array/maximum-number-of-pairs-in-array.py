class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hash = {}
        pair = 0
        leftOver = 0

        for n in nums:
            hash[n] = hash.get(n, 0) + 1

        for n in hash.values():
            pair += n//2
            leftOver += n%2

        return [pair, leftOver]

        