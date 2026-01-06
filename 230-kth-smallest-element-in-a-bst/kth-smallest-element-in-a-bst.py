# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        cnt = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cnt += 1
            if cnt==k:
                return cur.val
            else:
                cur = cur.right
        #O(n)
        #O(n)
        
        '''
        store and sort and take kth element
        O(n)+O(nlogn)
        O(n)
        '''

        '''
        perform inorder traversal and find kth element
        O(n)
        O(n)
        '''
        
        #O(n)
        #O(n)