class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        erase = 0
        intervals.sort(key=lambda x:x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0]<prev[1]:
                prev[1] = min(prev[1], interval[1])
                erase += 1
            else:
                prev = interval

        return erase
