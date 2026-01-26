class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        perm = []

        def helper():
            if len(perm)==n:
                res.append(perm[:])
                return
            for x in nums:
                if x not in perm:
                    perm.append(x)
                    helper()
                    perm.pop()
        
        helper()
        return res
        