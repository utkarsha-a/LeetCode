class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        c = False

        for i in s:
            if i !=" ":
                if not c:
                    c = True
                    l = 1
                else:
                    l +=1
            else:
                c = False
        return l
        