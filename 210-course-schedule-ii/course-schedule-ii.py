class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses
        order = []

        def dfs(node):
            if states[node]==visiting:
                return False
            elif states[node]==visited:
                return True
            states[node] = visiting
            for neig in adj[node]:
                if not dfs(neig):
                    return False
            states[node] = visited
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
            

        