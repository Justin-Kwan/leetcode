class Solution:
    # approach: literally buy low, sell high, like dumb robot
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        minPriceSoFar = float('inf')

        for currPrice in prices:
            # keep repositioning to new buy price if lower than min price so far
            if currPrice < minPriceSoFar:
                minPriceSoFar = currPrice
            # execute trade on first price > than min price so far
            else:
                # add to total profit
                totalProfit += (currPrice - minPriceSoFar)
                # reposition buy to current price to avoid overlapping transactions
                minPriceSoFar = currPrice

        return totalProfit

