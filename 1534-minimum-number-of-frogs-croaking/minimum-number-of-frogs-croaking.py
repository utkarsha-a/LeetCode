class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c,r,o,a,k, in_use, ans = 0,0,0,0,0,0,0
        for i in croakOfFrogs:
            if i=='c':
                c += 1
                in_use += 1
            elif i=='r':
                r += 1
            elif i=='o':
                o += 1
            elif i=='a':
                a += 1
            else:
                k += 1
                in_use -= 1
            
            ans = max(ans, in_use)

            if c<r or r<o or o<a or a<k:
                return -1
            
        if in_use==0 and c==r and r==o and o==a and a==k:
            return ans
        
        return -1
        