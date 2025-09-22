class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def helper(idx, cur, tot):
            if tot==target:
                res.append(cur[:])
                return
            if idx>=n or tot>target:
                return

            cur.append(candidates[idx])
            helper(idx, cur, tot+candidates[idx])
            cur.pop()
            helper(idx+1, cur, tot)

        helper(0, [], 0)

        return res
        