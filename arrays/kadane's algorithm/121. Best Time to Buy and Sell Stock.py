class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        Can be solved using Kadane's Algorithm
        '''

        #The profit is Calculated by profit[i]-profit[i-1]

        max_profit = 0
        best = 0

        for i in range(1,len(prices)):
            
            current_profit = prices[i]-prices[i-1]
            max_profit = max(current_profit,max_profit+current_profit)
            best = max(best , max_profit)

        return best



# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.