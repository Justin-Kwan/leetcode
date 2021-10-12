class Solution:
    # optimized sorted set of N frequency buckets
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsByFrequency = {}

        # build frequency map
        for num in nums:
            if num not in numsByFrequency:
                numsByFrequency[num] = 1
            else:
                numsByFrequency[num] += 1

        numFrequencyBuckets: List[List[int]] = [[] for i in range(len(nums))]

        # build sorted set of frequency buckets
        for num, frequency in numsByFrequency.items():
            numFrequencyBuckets[frequency - 1].append(num)

        topKFrequentNums = []

        # retrieve top k numbers from sorted set of buckets
        for i in range(len(numFrequencyBuckets) - 1, -1, -1):      # traverse buckets
            for num in numFrequencyBuckets[i]:                     # traverse elements in bucket
                if len(topKFrequentNums) >= k:
                    return topKFrequentNums

                topKFrequentNums.append(num)

        return topKFrequentNums

#     # max heap top K retrieval
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         numsByFrequency = {}

#         # dump number frequencies in map
#         for num in nums:
#             if num not in numsByFrequency:
#                 numsByFrequency[num] = (1, num) # store tuple for indexability in heap
#             else:
#                 numsByFrequency[num] = (numsByFrequency[num][0] + 1, num)

#         maxFrequencies = list(numsByFrequency.values())
#         heapq._heapify_max(maxFrequencies)

#         topKFrequentNums = []

#         # assuming maxFrequencies size >= k
#         for _ in range(0, k):
#             frequentNum = heapq._heappop_max(maxFrequencies)[1]
#             topKFrequentNums.append(frequentNum)

#         return topKFrequentNums
