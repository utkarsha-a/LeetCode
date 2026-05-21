class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if adj[crs] == []:
                return True
            
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
        '''
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state==visited:
                return True
            elif state==visiting:
                return False

            states[node] = visiting
            for neig in adj[node]:
                if not dfs(neig):
                    return False
            states[node] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
        #O(V+E)
        #O(V+E)
        '''
        