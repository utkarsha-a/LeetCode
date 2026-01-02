# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 0))
        m = 0
        while q:
            n = len(q)
            l = q[0][1]
            r = q[-1][1]
            m = max(m, r-l+1)
            for i in range(n):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, 2*idx+1))
                if node.right:
                    q.append((node.right, 2*idx+2))
        return m
