class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def helper(i):
            if i>=len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    helper(j+1)
                    part.pop()

        helper(0)
        return res

    def isPalindrome(self, s, l, r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

        '''
        if not s:
            return [[]]
        ans = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)
        return ans
        '''