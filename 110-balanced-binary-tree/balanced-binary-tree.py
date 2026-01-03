# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(node):
            if not node:
                return 0 
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal balanced
            if abs(r-l)>1:
                balanced = False
                return 0
            return max(l, r)+1
        dfs(root)
        return balanced
            


        