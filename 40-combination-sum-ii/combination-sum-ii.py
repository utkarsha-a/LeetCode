class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def helper(idx, cur, tot):
            if tot==target:
                res.append(cur[:])
                return
            if idx>=n or tot>target:
                return 
            
            cur.append(candidates[idx])
            helper(idx+1, cur, tot+candidates[idx])
            cur.pop()

            while idx+1<n and candidates[idx]==candidates[idx+1]:
                idx+=1
            helper(idx+1, cur, tot)

        helper(0, [], 0)
        return res