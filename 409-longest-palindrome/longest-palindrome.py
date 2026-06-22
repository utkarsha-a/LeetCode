class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmp = {}

        for ch in s:
            hashmp[ch] = hashmp.get(ch, 0) + 1
        
        longest = 0
        odd_found = 0

        for n in hashmp.values():
            longest += n - (n%2)
            if n%2==1:
                odd_found = True

        if odd_found:
            longest += 1

        return longest