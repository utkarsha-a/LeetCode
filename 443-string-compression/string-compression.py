class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0

        while i<len(chars):
            letter = chars[i]
            cnt = 0
            while i<len(chars) and chars[i]==letter:
                cnt += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if cnt>1:
                for c in str(cnt):
                    chars[ans] = c
                    ans += 1
        return ans    
        