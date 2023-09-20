class Solution {
public:
    // bottom up dp approach
    int coinChange(vector<int> &coins, int amount) {
        // build up solution of minimum coins needed to make each amount, default to not
        // possible initially and zero coins trivially needed to make amount of 0
        vector<int> minCoinsByAmount(amount + 1, INT_MAX);
        minCoinsByAmount[0] = 0;

        for (int curAmount = 1; curAmount <= amount; ++curAmount) {
            for (int &coin : coins) {
                // cannot make current amount with current coin (exceeds amount)
                if (curAmount - coin < 0) {
                    continue;
                }

                // minimum number of coins (steps) to make current amount depends on the
                // minimum number of coins to make amount one coin denomination away if
                // possible (+ 1 coin including current)
                minCoinsByAmount[curAmount] = min(minCoinsByAmount[curAmount - coin], minCoinsByAmount[curAmount]);
            }

            // only add back coin to make current amount possible to make previous amount
            if (minCoinsByAmount[curAmount] < INT_MAX) {
                ++minCoinsByAmount[curAmount];
            }
        }

        int minCoins = minCoinsByAmount[amount];
        return minCoins == INT_MAX ? -1 : minCoins;
    }

    // // top down dp approach
    // int coinChange(vector<int> &coins, int amount) {
    //     // cache minimum number of coins needed to make each unique amount
    //     unordered_map<int, int> cache;
    //     int minCoins = minRequiredCoins(coins, amount, cache);
    //     return minCoins == INT_MAX ? -1 : minCoins;
    // }

    // int minRequiredCoins(vector<int> &coins, int amount, unordered_map<int, int> &cache) {
    //     // previous coin used does not make exact change (exceeds amount)
    //     if (amount < 0) {
    //         return INT_MAX;
    //     }
    //     // zero coins trivially needed to make amount of 0
    //     if (amount == 0) {
    //         return 0;
    //     }

    //     // previously computed minimum number of coins to make current amount
    //     if (cache.find(amount) != cache.end()) {
    //         return cache[amount];
    //     }

    //     // minimum number of coins to make current amount depends on minimum coins to
    //     // make amount one coin denomination away (+ 1 coin including current)
    //     int minCoinsNextAmount = INT_MAX;
    //     for (int &coin : coins) {
    //         minCoinsNextAmount = min(minCoinsNextAmount, minRequiredCoins(coins, amount - coin, cache));
    //     }

    //     // only add back coin to make current amount possible to make previous amount
    //     if (minCoinsNextAmount < INT_MAX) {
    //         ++minCoinsNextAmount;
    //     }
    //     cache[amount] = minCoinsNextAmount;

    //     return minCoinsNextAmount;
    // }
};
