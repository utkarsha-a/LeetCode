class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))

        events.sort()

        res = [[0, 0]]
        hp = [(0, float("inf"))]
        
        for pos, negH, R in events:
            while hp[0][1] <= pos:
                heapq.heappop(hp)
            if negH != 0:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] != -hp[0][0]:
                res.append([pos, -hp[0][0]])
        
        return res[1:]