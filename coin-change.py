class Solution:
    
    # brute force
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         if amount == 0:
#             return 0
#         if amount < 0:
#             return -1

#         minCoinsUsedSoFar = float('inf')

#         for coin in coins:
#             currCoinsUsed = self.coinChange(coins, amount - coin)
            
#             if currCoinsUsed == -1:
#                 continue;
                
#             if currCoinsUsed + 1 < minCoinsUsedSoFar:
#                 minCoinsUsedSoFar = currCoinsUsed + 1

#         if minCoinsUsedSoFar == float('inf'):
#             return -1

#         return minCoinsUsedSoFar

    # optomized (memoized)
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        return self.recurseCountCoins(coins, amount, cache)

    def recurseCountCoins(self, coins: List[int], amount: int, cache: Dict[int, int]) -> int:

        if amount == 0:
            return 0
        if amount < 0:
            return -1

        minCoinsUsedSoFar = float('inf')
        
        # hit cache for min coins to reach amount
        if amount in cache:
            return cache[amount]

        for coin in coins:
            currCoinsUsed = self.recurseCountCoins(coins, amount - coin, cache)

            # ignore all coins where amount cannot be reached
            if currCoinsUsed == -1:
                continue;
                
            # otherwise with valid coins to get to amount, overtake current min needed
            if currCoinsUsed + 1 < minCoinsUsedSoFar:
                minCoinsUsedSoFar = currCoinsUsed + 1
        
        # if all amount subtract by all coins cannot reach amount (all -1 returned)
        if minCoinsUsedSoFar == float('inf'):
            cache[amount] = -1
            return -1

        # update cache on way out
        cache[amount] = minCoinsUsedSoFar

        return minCoinsUsedSoFar
