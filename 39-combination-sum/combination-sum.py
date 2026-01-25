class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        n = len(candidates)
        
        def helper(idx, tot):
            if tot==target:
                res.append(sub[:])
                return
            if idx>=n or tot>target:
                return

            sub.append(candidates[idx])
            helper(idx, tot+candidates[idx])
            sub.pop()
            helper(idx+1, tot)
        
        helper(0,0)
        return res