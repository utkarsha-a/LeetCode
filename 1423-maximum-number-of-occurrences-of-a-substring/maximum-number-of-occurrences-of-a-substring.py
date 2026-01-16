class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        freq = defaultdict(int)
        char_cnt = defaultdict(int)
        unique = 0
        res = 0
        left = 0

        for right in range(n):
            char_cnt[s[right]] += 1
            if char_cnt[s[right]] == 1:
                unique += 1

            if right-left+1 > minSize:
                char_cnt[s[left]] -= 1
                if char_cnt[s[left]] == 0:
                    unique -= 1
                left += 1

            if right-left+1 == minSize and unique<=maxLetters:
                substr = s[left:right+1]
                freq[substr] += 1
                res = max(res, freq[substr])

        return res