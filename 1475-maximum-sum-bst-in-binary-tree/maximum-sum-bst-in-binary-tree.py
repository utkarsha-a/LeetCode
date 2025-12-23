# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return 1, float('inf'), float('-inf'), 0

            lbst, lmin, lmax, lsum = dfs(node.left)
            rbst, rmin, rmax, rsum = dfs(node.right)

            if lbst and rbst and lmax< node.val< rmin:
                cursum = lsum+rsum+node.val

                nonlocal maxsum
                maxsum = max(maxsum, cursum)

                return (1, min(lmin,node.val), max(node.val, rmax), cursum)
            
            return 0,0,0,0

        maxsum = 0
        dfs(root)
        return maxsum

        