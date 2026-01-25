class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        n = len(nums)        

        def helper(idx):
            if idx==n:
                res.append(sub[:])
                return
            sub.append(nums[idx])
            helper(idx+1)

            sub.pop()
            helper(idx+1)

        helper(0)
        return res