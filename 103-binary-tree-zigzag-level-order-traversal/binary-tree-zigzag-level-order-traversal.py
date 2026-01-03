# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        l = 0

        while q:
            s = []
            l+=1
            for i in range(len(q)):
                node = q.popleft()
                s.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if l%2==1:
                res.append(s)
            if l%2==0:
                res.append(s[::-1])
        return res
        
        