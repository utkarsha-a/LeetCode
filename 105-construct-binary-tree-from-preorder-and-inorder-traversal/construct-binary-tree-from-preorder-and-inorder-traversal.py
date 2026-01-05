# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                i = inorder.index(preorder.popleft())
                root = TreeNode(inorder[i])
                root.left = build(preorder, inorder[:i])
                root.right = build(preorder, inorder[i+1:])

                return root

        return build(preorder, inorder) 
        #O(n^2)
        #O(n^2)
        '''
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i
        preorder = deque(preorder)

        def build(start, end):
            if start>end:
                return None
            root = TreeNode(preorder.popleft())
            mid = mp[root.val]
            root.left = build(start, mid-1)
            root.right = build(mid+1, end)

            return root
        
        return build(0, len(preorder)-1)