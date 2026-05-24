class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    res -= union(i, j)
        
        return res

        


'''        
class Solution:
    def dfs(self, node, adj, vis):
        vis[node] = True
        for neighbor in adj[node]:
            if not vis[neighbor]:
                self.dfs(neighbor, adj, vis)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
                    adj[j].append(i)

        vis = [False] * n
        count = 0

        for i in range(n):
            if not vis[i]:
                self.dfs(i, adj, vis)
                count += 1

        return count
'''