class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        @cache
        def longest(i,j):
            if i==m or j==n:
                return 0
            elif text1[i]==text2[j]:
                return 1+longest(i+1,j+1)
            else:
                return max(longest(i+1, j), longest(i,j+1))

        return longest(0,0)            

        