class Solution:
    # approach: literally buy low, sell high, like dumb robot
    def maxProfit(self, prices: List[int]) -> int:
        totalMaxProfit = 0
        buyPrice = float("inf")

        for price in prices:
            # keep repositioning on smaller buy price
            if price < buyPrice:
                buyPrice = price
            # take local max profit on first price larger than buy price, and add it
            # to total max profit
            else:
                totalMaxProfit += price - buyPrice
                # reposition to buy price to current price to avoid overlapping transactions
                # involving multiple shares
                #
                # making multiple transactions always yields same or more profit than single
                # transaction (draw lines to prove so)
                buyPrice = price

        return totalMaxProfit
