class Solution:
    # max heap top K retrieval
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsByFrequency = {}

        # dump number frequencies in map
        for num in nums:
            if num not in numsByFrequency:
                numsByFrequency[num] = (1, num) # store tuple for indexability in heap
            else:
                numsByFrequency[num] = (numsByFrequency[num][0] + 1, num)

        maxFrequencies = list(numsByFrequency.values())
        heapq._heapify_max(maxFrequencies)

        topKFrequentNums = []

        # assuming maxFrequencies size >= k
        for _ in range(0, k):
            frequentNum = heapq._heappop_max(maxFrequencies)[1]
            topKFrequentNums.append(frequentNum)

        return topKFrequentNums
