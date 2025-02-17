class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        tot_candies = n
        i = 1

        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            
            peak = 0
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                tot_candies += peak
                i += 1
            
            if i == n:
                return tot_candies

            valley = 0
            while i < n and ratings[i] < ratings[i-1]:
                valley += 1
                tot_candies += valley
                i += 1
            tot_candies -= min(peak, valley)

        return tot_candies

        