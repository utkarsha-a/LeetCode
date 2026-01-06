# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        preorder = deque(preorder)

        def build(preorder, inorder):
            if not inorder:
                return None
            
            rootval = preorder.popleft()
            root = TreeNode(rootval)
            idx = inorder.index(rootval)
            
            root.left = build(preorder, inorder[:idx])
            root.right = build(preorder, inorder[idx+1:])
            return root
        return build(preorder, inorder)
            

