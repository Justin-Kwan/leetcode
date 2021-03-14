class Solution:
    
    # optimal (peak and valley)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitSoFar = 0
        minPriceSoFar = float('inf')
        
        for currPrice in prices:
            # each price either overtakes the min price so far
            if currPrice < minPriceSoFar:
                minPriceSoFar = currPrice
            # or compares against the min price so far to take profit
            else:
                currProfit = currPrice - minPriceSoFar
                maxProfitSoFar = max(maxProfitSoFar, currProfit)
    
        return maxProfitSoFar

    # test cases
    # assert maxProfit([1]) == 0
    # assert maxProfit([7,6,4,3,1]) == 0    |     -1
    # assert maxProfit([7,1,5,3,6,4]) == 5
