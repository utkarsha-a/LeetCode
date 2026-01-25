class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        n = len(candidates)
        candidates.sort()

        def helper(idx, tot):
            if tot==target:
                res.append(sub[:])
                return 
            if idx>=n or tot>target:
                return 

            sub.append(candidates[idx])
            helper(idx+1, tot+candidates[idx])
            
            sub.pop()
            while idx+1<n and candidates[idx]==candidates[idx+1]:
                idx+=1
            helper(idx+1, tot)

        helper(0, 0)
        return res