class Solution:
    def checkValidString(self, s: str) -> bool:
        open_st = []
        star_st = []

        for i, ch in enumerate(s):
            if ch == '(':
                open_st.append(i)
            elif ch == '*':
                star_st.append(i)
            elif ch == ')':
                if open_st:
                    open_st.pop()
                elif star_st:
                    star_st.pop()
                else:
                    return False
        
        while open_st and star_st:
            if open_st[-1] < star_st[-1]:
                open_st.pop()
                star_st.pop()
            else:
                return False
        
        return len(open_st) == 0

        
            
        