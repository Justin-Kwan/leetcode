class Solution:
    # optimal case analysis approach
    def maxProfit(self, prices: List[int]) -> int:
        # find max global profit in stock price sequence
        transaction = []
        maxProfit = self.maxGlobalProfit(prices, transaction)
        buyDate, sellDate = transaction[0], transaction[1]

        # search for second most profitable transaction to left and right of
        # global one
        maxLeftProfit = self.maxGlobalProfit(prices[:buyDate], [])
        maxRightProfit = self.maxGlobalProfit(prices[sellDate + 1:], [])

        # search for max price loss within global max profit transaction
        transactionPrices = prices[buyDate: sellDate + 1]
        maxLossInTransaction = self.maxGlobalProfit(
            transactionPrices[::-1], [])

        # if global max profit transaction is non-decreasing, then return
        # it and the transaction to left or right with more profit (if exists)
        #
        # if global max profit transaction decreases, then the two max profit
        # transactions are either
        #  * global max transaction and max transaction to left or right
        #  * two transactions within global max transaction, seperated by the
        #    max loss price sequence (loss added to offset second subtransaction
        #    that starts at a lower price)
        return max(maxProfit, maxProfit + maxLeftProfit, maxProfit + maxRightProfit, maxProfit + maxLossInTransaction)

    def maxGlobalProfit(self, prices: List[int], transaction: List[int]) -> int:
        if not prices:
            return 0

        # default transaction buy and sell dates if no profit in prices
        transaction.extend((0, 0))
        minPrice = prices[0]
        maxProfit, lastBuyDate = 0, 0

        for i in range(len(prices)):
            # replace max profit with larger current, update buy and sell date
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
                transaction[0], transaction[1] = lastBuyDate, i
            # reposition to lower buy price, update *tentative* buy date
            if prices[i] < minPrice:
                lastBuyDate = i
                minPrice = prices[i]

        return maxProfit
