class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize our state variables
        min_price = float('inf')  # Start with infinity so any price will be lower
        max_profit = 0            # Start with 0 as the baseline profit
        
        for price in prices:
            # If we find a new historically low price, update min_price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today yields a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

            