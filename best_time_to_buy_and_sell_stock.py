class Solution:
    # optimal peak and valley approach
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = float("inf")

        for price in prices:
            # reposition to smaller buy price
            if price < buyPrice:
                buyPrice = price
            # otherwise take local max profit of current price against buy price
            # and compare against global max profit
            else:
                maxProfit = max(price - buyPrice, maxProfit)

        return maxProfit

    # test cases
    # assert maxProfit([1]) == 0
    # assert maxProfit([7,6,4,3,1]) == 0    |     -1
    # assert maxProfit([7,1,5,3,6,4]) == 5
