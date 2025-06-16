class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}

        for i, ch in enumerate(s):
            last_occurence[ch] = i

        res = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last_occurence[ch])

            if i == end:
                res.append(end-start+1)
                start = i+1

        return res
        