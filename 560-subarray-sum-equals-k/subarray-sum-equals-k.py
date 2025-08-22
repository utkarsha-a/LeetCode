class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0:1}
        tot = cnt = 0

        for n in nums:
            tot += n

            if tot-k in hash:
                cnt += hash[tot-k]

            hash[tot] = 1+hash.get(tot, 0)

        return cnt
        