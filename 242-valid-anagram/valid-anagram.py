class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}

        for c in s:
            mp[c] = mp.get(c, 0) + 1

        for d in t:
            mp[d] = mp.get(d, 0) - 1

        for n in mp:
            if mp[n] != 0:
                return False
        return True