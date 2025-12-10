class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] != ']':
                st.append(s[i])
            else:
                substr = ""
                while st[-1] != '[':
                    substr = st.pop() + substr
                st.pop()

                num = ""
                while st and st[-1].isdigit():
                    num = st.pop() + num
                st.append(int(num)*substr)
                
        return "".join(st)      