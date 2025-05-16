"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_same(x1, y1, size):
            val = grid[x1][y1]
            for i in range(x1, x1 + size):
                for j in range(y1, y1 + size):
                    if grid[i][j] != val:
                        return False
            return True

        def build(x1, y1, size):
            if is_same(x1, y1, size):
                return Node(val=bool(grid[x1][y1]), isLeaf=True)

            half = size // 2
            return Node(
                val=True,  # value doesnt matter when isLeaf is False
                isLeaf=False,
                topLeft=build(x1, y1, half),
                topRight=build(x1, y1 + half, half),
                bottomLeft=build(x1 + half, y1, half),
                bottomRight=build(x1 + half, y1 + half, half)
            )

        n = len(grid)
        return build(0, 0, n)
        