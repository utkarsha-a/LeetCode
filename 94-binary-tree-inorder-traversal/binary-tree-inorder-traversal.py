# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        result = []
        
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result
        '''
        res = []
        cur = root

        while cur is not None:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right is not None and prev.right!=cur:
                    prev = prev.right
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res


        