# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction 
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Solution by Molly Yu


class Solution(object):
    # First Attempt
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            sell = max(prices[i:len(prices)])
            if buy < sell:
                profit = max(profit, sell - buy)
        return profit

    # Another solution, not requiring new List
    def maxProfit2(self, prices):
        if not prices:
            return 0
        profit = 0
        minPrice = prices[0]
        for price in prices: # think of price as the selling price
            minPrice = min(minPrice, price) # minPrice is buying price
            profit = max(profit, (price - minPrice))
        return profit   
                

