class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices) - 1):
        # If tomorrow's price is lower, we consider today a selling day.
           if prices[i] < prices[i + 1] :
                profit += prices[i+1] - prices[i]
               
        return profit
                
            
        