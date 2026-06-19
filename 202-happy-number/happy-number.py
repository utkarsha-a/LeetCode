class Solution:
    def isHappy(self, n: int) -> bool:
        # LINKED LIST APPROACH DOES NOT TAKE MEMORY
        slow = n
        fast = n
        while True:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        
            if slow==1:
                return True
            
            if slow==fast:
                return False
        '''
        # SET APPROACH, TAKES MEMORRY OF O(N)
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n==1:
                return True
        return False
        '''

    def sumOfSquares(self, n):
        output = 0
        while n!=0:
            digit = (n%10)**2
            output += digit
            n = n//10
        return output