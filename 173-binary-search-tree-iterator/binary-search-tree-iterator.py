# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.i = 0
        self.ls = []
        self.inorder(root)

    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.ls.append(root.val)
        self.inorder(root.right) 

    def next(self) -> int:
        val = self.ls[self.i]
        self.i += 1
        return val      

    def hasNext(self) -> bool:
        if self.i < len(self.ls):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()