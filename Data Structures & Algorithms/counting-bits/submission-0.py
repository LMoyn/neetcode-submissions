class Solution:
    def countBits(self, n: int) -> List[int]:
        

        #Simple solution: loop and recalculate each time

        out = [0]*(n+1)

        for j in range(n+1):
            count = 0
            i = j
            while i > 0:
                if i%2:
                    count = count+1
                i = (i - (i%2))/2

            out[j] = count

        #More advanced solution: use DP

        return out