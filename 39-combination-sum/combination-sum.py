class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def make_comb(idx, com, tot):
            if tot == target:
                res.append(com[:])
                return
            
            if tot > target or idx >= len(candidates):
                return

            com.append(candidates[idx])
            make_comb(idx, com, tot+candidates[idx])
            com.pop()
            make_comb(idx+1, com, tot)

            return res
        return make_comb(0,[],0)
        