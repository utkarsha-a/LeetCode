class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph) # odd=1 and even=-1
        
        def bfs(i):
            if odd[i]:
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                i = q.popleft()
                for neig in graph[i]:
                    if odd[neig] and odd[i]==odd[neig]:
                        return False
                    elif not odd[neig]:
                        q.append(neig)
                        odd[neig] = odd[i] * -1
            return True

        for j in range(len(graph)):
            if not bfs(j):
                return False
        return True


        