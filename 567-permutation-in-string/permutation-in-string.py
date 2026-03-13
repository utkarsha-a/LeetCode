class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False
        
        mp1 = [0]*26
        mp2 = [0]*26

        for i in range(n1):
            mp1[ord(s1[i])-97] += 1
            mp2[ord(s2[i])-97] += 1

        if mp1==mp2:
            return True
        
        for i in range(n1, n2):
            mp2[ord(s2[i])-97] += 1
            mp2[ord(s2[i-n1]) - ord('a')] -= 1

            if mp1==mp2:
                return True

        return False

        #O(n2), O(1)