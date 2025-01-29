# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        min_dif = float("inf")
        prev = float("inf")

        def traverse(node): 
            nonlocal min_dif, prev
            if not node: 
                return 
            traverse(node.left)
            min_dif = min(min_dif, abs(prev - node.val))
            prev = node.val
            traverse(node.right)

        traverse(root)
        return min_dif
        