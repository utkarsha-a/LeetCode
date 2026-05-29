class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        #reverse sort so we can pop smallest destination from the end
        tickets.sort(reverse=True)

        for src, dst in tickets:
            adj[src].append(dst)

        itinerary = []

        def dfs(src):
            while adj[src]:
                nxt = adj[src].pop()
                dfs(nxt)

            itinerary.append(src)

        dfs("JFK")

        return itinerary[::-1]
        '''
        adj = defaultdict(list)
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src]) # creating copy to not modify the main list
            for idx, v in enumerate(temp):
                adj[src].pop(idx)
                res.append(v)

                if dfs(v):
                    return True

                adj[src].insert(idx, v)
                res.pop()
            return False

        dfs("JFK")
        return res
        '''