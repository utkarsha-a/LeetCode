# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced= [True]

        def height(root):
            if not root:
                return True
            left = height(root.left)
            right = height(root.right)
            if abs(left-right)>1:
                balanced[0] = False
                return 0
            
            return 1+max(left, right)

        height(root)
        return balanced[0] 

            


        