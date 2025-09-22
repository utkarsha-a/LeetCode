class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []

        def helper(idx):
            if idx==n:
                res.append(subset[:])
                return

            subset.append(nums[idx])
            helper(idx+1)

            subset.pop()
            helper(idx+1)

        helper(0)
        return res
        