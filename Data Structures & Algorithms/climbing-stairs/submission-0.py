class Solution:
    def climbStairs(self, n: int) -> int:
        #memoize
        if n == 1:
            return 1
        if n == 2:
            return 2
    
        shift_1 = 1
        index = 3
        current = 2
        while index <= n:
            current_store = current
            current = shift_1 + current
            shift_1 = current_store
            index = index+1

        return current