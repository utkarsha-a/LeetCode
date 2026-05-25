class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(x):
            while x!=parent[x]:
                x = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1==p2:
                return False
            
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
