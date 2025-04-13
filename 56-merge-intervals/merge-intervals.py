class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for i in intervals[1:]:
            if i[0] <= prev[1]:
                prev[1] = max(prev[1], i[1])
            else:
                merged.append(prev)
                prev = i

        merged.append(prev)

        return merged

        