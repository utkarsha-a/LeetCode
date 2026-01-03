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

        l = True

        while q:
            s = []

            for i in range(len(q)):
                node = q.popleft()
                s.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if l:
                res.append(s)
            if not l:
                res.append(s[::-1])
            l = not l

        return res
        