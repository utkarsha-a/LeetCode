class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        arr = list(s)
        l = 0
        r = len(s)-1
        while l<r:
            if arr[l] != arr[r]:
                smaller = min(arr[l], arr[r])
                arr[l], arr[r] = smaller, smaller
            l += 1
            r -= 1
        
        return ''.join(arr)
        