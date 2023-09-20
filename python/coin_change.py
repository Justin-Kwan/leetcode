class Solution:
    # # brute force
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # cannot use coin path to make original amount
    #     if amount < 0:
    #         return -1
    #     # can use coin path to make original amount,
    #     # since it takes 0 coins to make 0 amount
    #     if amount == 0:
    #         return 0

    #     # min coin count needed to make amount up to now
    #     minCoinCountSoFar = float('inf')

    #     # find min coin combination needed to make current amount
    #     for coin in coins:
    #         coinCount = self.coinChange(coins, amount - coin)

    #         if coinCount == -1:
    #             continue

    #         minCoinCountSoFar = min(coinCount, minCoinCountSoFar)

    #     # if no valid coin paths to reach current amount
    #     if minCoinCountSoFar == float('inf'):
    #         return -1

    #     # add 1 coin to account for lost coin during subtraction
    #     return minCoinCountSoFar + 1

    # # optimized (memoized)
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     return self.countCoinChange(coins, amount, {})

    # def countCoinChange(self, coins: List[int], amount: int, minChangeByAmount: dict[int, int]) -> int:
    #     # cannot use coin path to make original amount
    #     if amount < 0:
    #         return -1
    #     # can use coin path to make original amount,
    #     # since it takes 0 coins to make 0 amount
    #     if amount == 0:
    #         return 0

    #     # try hitting cache for min coin change at amount
    #     if amount in minChangeByAmount:
    #         return minChangeByAmount[amount]

    #     # min coin count needed to make amount up to now
    #     minCoinCountSoFar = float('inf')

    #     # find min coin combination needed to make current amount
    #     for coin in coins:
    #         coinCount = self.countCoinChange(coins, amount - coin, minChangeByAmount)

    #         if coinCount == -1:
    #             continue

    #         minCoinCountSoFar = min(coinCount, minCoinCountSoFar)

    #     # if no valid coin paths to reach current amount
    #     if minCoinCountSoFar == float('inf'):
    #         minChangeByAmount[amount] = -1
    #         return -1

    #     # update cache with min coin change at amount
    #     minChangeByAmount[amount] = minCoinCountSoFar + 1

    #     # add 1 coin to account for lost coin during subtraction
    #     return minCoinCountSoFar + 1

    # optimal bottom up dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        minSteps = []
        minSteps.append(0) # it takes 0 steps to get to 0
        
        for currAmount in range(1, amount + 1):
            # placeholder
            minSteps.append(float("inf"))
            for coin in coins:
                # cannot subtract to get subproblem
                if coin > currAmount:
                    continue
                # find subproblem (the difference by subtracting the coin)
                diff = currAmount - coin
                # least num of steps to get currAmount is the smallest
                # between least num of steps to get subproblem + 1 (to account                     # for coin that gets us to subproblem) or current num of steps                     # already
                minSteps[currAmount] = min(minSteps[diff] + 1, minSteps[currAmount])

        # if amount cannot be made up of the coins 
        # (inf is propagated from subproblems, or by all and amount)
        if minSteps[amount] == float("inf"):
            return -1

        # min num of steps/coins to get amount
        return minSteps[amount]
