class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_hash = {}

        for c in magazine:
            mag_hash[c] = 1 + mag_hash.get(c,0)

        for c in ransomNote:
            if c not in mag_hash or mag_hash[c] <=0:
                return False
            mag_hash[c] -= 1
        return True
        