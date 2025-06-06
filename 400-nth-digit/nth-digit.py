class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        seq = ""
        i = 1
        while len(seq) < n:
            seq += str(i)
            i += 1
        return int(seq[n-1])
        '''

        i = 1
        start = 1
        end = 9

        while n > i * end:
            n -= i*end
            i += 1
            end *= 10
            start *= 10

        num = start + (n-1)//i
        return int(str(num)[(n-1)%i])

        