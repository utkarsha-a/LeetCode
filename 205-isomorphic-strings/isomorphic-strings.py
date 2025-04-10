class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        index_s = {}
        index_t = {}

        for i in range(len(s)):
            if s[i] not in index_s:
                index_s[s[i]] = i

            if t[i] not in index_t:
                index_t[t[i]] = i

            if index_s[s[i]] != index_t[t[i]]:
                return False

        return True

        
        