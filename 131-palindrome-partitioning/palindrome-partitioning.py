class Solution:
    def isPalindrome(self, s, i, j):
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        n = len(s)

        def helper(idx):
            if idx >= n:
                res.append(part[:])
                return 
            for j in range(idx, n):
                if self.isPalindrome(s, idx, j):
                    part.append(s[idx:j+1])
                    helper(j+1)
                    part.pop()

        helper(0)
        return res

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