class Solution:
    def reverseBits(self, n: int) -> int:
        sum = 0
        
        exp = 0
        while n > 0:
            if n%2:
                sum += 2**(31-exp)
                n = n-1
            n = n/2
            exp+=1

        return sum