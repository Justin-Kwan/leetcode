class Solution:
    # bottom up dp approach
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # carry over min price to left, max price to right of each trading day
        minLeftPrice, maxLeftProfits = prices[0], [0] * len(prices)
        maxRightPrice, maxRightProfits = prices[len(
            prices) - 1], [0] * len(prices)

        # compute subproblems of max transaction prices to left and right
        # of each trading day
        for left in range(1, len(prices)):
            right = len(prices) - left - 1
            # compute max transaction profit to left of current price
            minLeftPrice = min(minLeftPrice, prices[left - 1])
            maxProfitEndingAtPrice = prices[left] - minLeftPrice
            maxLeftProfits[left] = max(
                maxLeftProfits[left - 1], maxProfitEndingAtPrice)
            # compute max transaction profit to right of current price
            maxRightPrice = max(maxRightPrice, prices[right + 1])
            maxProfitStartingAtPrice = maxRightPrice - prices[right]
            maxRightProfits[right] = max(
                maxProfitStartingAtPrice, maxRightProfits[right + 1])

        # find the max left and right transaction profits of a trading day
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, maxLeftProfits[i] + maxRightProfits[i])

        return maxProfit

    # # optimal case analysis approach
    # def maxProfit(self, prices: List[int]) -> int:
    #     # find max global profit in stock price sequence
    #     transaction = []
    #     maxProfit = self.maxGlobalProfit(prices, transaction)
    #     buyDate, sellDate = transaction[0], transaction[1]

    #     # search for second most profitable transaction to left and right of
    #     # global one
    #     maxLeftProfit = self.maxGlobalProfit(prices[:buyDate], [])
    #     maxRightProfit = self.maxGlobalProfit(prices[sellDate + 1:], [])

    #     # search for max price loss within global max profit transaction
    #     transactionPrices = prices[buyDate:sellDate + 1]
    #     maxLossInTransaction = self.maxGlobalProfit(transactionPrices[::-1], [])

    #     # if global max profit transaction is non-decreasing, then return
    #     # it and the transaction to left or right with more profit (if exists)
    #     #
    #     # if global max profit transaction decreases, then the two max profit
    #     # transactions are either
    #     #  * global max transaction and max transaction to left or right
    #     #  * two transactions within global max transaction, seperated by the
    #     #    max loss price sequence (loss added to offset second subtransaction
    #     #    that starts at a lower price)
    #     return max(maxProfit, maxProfit + maxLeftProfit, maxProfit + maxRightProfit, maxProfit + maxLossInTransaction)

    # def maxGlobalProfit(self, prices: List[int], transaction: List[int]) -> int:
    #     if not prices:
    #         return 0

    #     # default transaction buy and sell dates if no profit in prices
    #     transaction.extend((0, 0))
    #     minPrice = prices[0]
    #     maxProfit, lastBuyDate = 0, 0

    #     for i in range(len(prices)):
    #         # replace max profit with larger current, update buy and sell date
    #         if prices[i] - minPrice > maxProfit:
    #             maxProfit = prices[i] - minPrice
    #             transaction[0], transaction[1] = lastBuyDate, i
    #         # reposition to lower buy price, update *tentative* buy date
    #         if prices[i] < minPrice:
    #             lastBuyDate = i
    #             minPrice = prices[i]

    #     return maxProfit
