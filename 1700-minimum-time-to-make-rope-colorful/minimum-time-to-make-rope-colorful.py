class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tot = 0
        maxx = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i-1] == colors[i]:
                tot += min(maxx, neededTime[i])
                maxx = max(maxx, neededTime[i])
            else:
                maxx = neededTime[i]
        
        return tot


        