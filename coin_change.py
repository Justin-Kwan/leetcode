class Solution:
#     # brute force
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # cannot use coin path to make original amount
#         if amount < 0:
#             return -1
#         # can use coin path to make original amount,
#         # since it takes 0 coins to make 0 amount
#         if amount == 0:
#             return 0

#         # min coin count needed to make amount up to now
#         minCoinCountSoFar = float('inf')

#         # find min coin combination needed to make current amount
#         for coin in coins:
#             coinCount = self.coinChange(coins, amount - coin)

#             if coinCount == -1:
#                 continue

#             minCoinCountSoFar = min(coinCount, minCoinCountSoFar)

#         # if no valid coin paths to reach current amount
#         if minCoinCountSoFar == float('inf'):
#             return -1

#         # add 1 coin to account for lost coin during subtraction
#         return minCoinCountSoFar + 1

    # optimized (memoized)
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.countCoinChange(coins, amount, {})

    def countCoinChange(self, coins: List[int], amount: int, minChangeByAmount: dict[int, int]) -> int:
        # cannot use coin path to make original amount
        if amount < 0:
            return -1
        # can use coin path to make original amount,
        # since it takes 0 coins to make 0 amount
        if amount == 0:
            return 0

        # try hitting cache for min coin change at amount
        if amount in minChangeByAmount:
            return minChangeByAmount[amount]

        # min coin count needed to make amount up to now
        minCoinCountSoFar = float('inf')

        # find min coin combination needed to make current amount
        for coin in coins:
            coinCount = self.countCoinChange(coins, amount - coin, minChangeByAmount)

            if coinCount == -1:
                continue

            minCoinCountSoFar = min(coinCount, minCoinCountSoFar)

        # if no valid coin paths to reach current amount
        if minCoinCountSoFar == float('inf'):
            minChangeByAmount[amount] = -1
            return -1

        # update cache with min coin change at amount
        minChangeByAmount[amount] = minCoinCountSoFar + 1

        # add 1 coin to account for lost coin during subtraction
        return minCoinCountSoFar + 1

