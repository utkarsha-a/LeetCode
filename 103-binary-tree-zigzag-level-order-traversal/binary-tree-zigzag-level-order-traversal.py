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
        queue = deque([root])
        is_l_to_r = True

        while queue:
            level_size = len(queue)
            cur_level = [0]*level_size

            for i in range(level_size):
                node = queue.popleft()
                if is_l_to_r:
                    index = i
                else:
                    index = level_size-1-i
                cur_level[index] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)
            is_l_to_r = not is_l_to_r

        return res 