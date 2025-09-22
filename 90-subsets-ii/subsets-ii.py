class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sub = []
        nums.sort()

        def helper(idx):
            if idx==n:
                res.append(sub[:])
                return 
            
            sub.append(nums[idx])
            helper(idx+1)
            sub.pop()

            while idx+1<n and nums[idx]==nums[idx+1]:
                idx += 1
                
            helper(idx+1)

        helper(0)
        return res
        