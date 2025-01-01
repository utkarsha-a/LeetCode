class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Convert wordDict to a set for O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)  # DP array to store results
        dp[0] = True  # Empty string is always a valid segmentation
        
        # Iterate over all lengths of substrings
        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[j:i] is a word and dp[j] is True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
        