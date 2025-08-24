class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
            
        repeatA = a
        count = 1

        while len(repeatA) < len(b):
            repeatA += a
            count += 1
            if b in repeatA:
                return count

        repeatA += a
        count += 1
        if b in repeatA:
            return count

        return -1
        