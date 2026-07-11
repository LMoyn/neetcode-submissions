class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        #key point: if we do this by iterating sell time
            #buy will always be min before that
            #so either previous min is buy, or position right before the sell time iterated over

        profit = 0
        buy = prices[0]

        for r in range(len(prices)-1):
            r = r+1
            buy = min(buy,prices[r-1])
            profit = max(profit,prices[r]-buy)

        return profit