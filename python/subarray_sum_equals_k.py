class Solution:
    # optimal prefix sum approach
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum of 0 should exist ST k complement of 0 exists when
        # first element is k or entire array sums to k
        prefixSumsByFreq = {0: 1}
        currentSum = 0
        subarraySumCount = 0

        # must build prefix sums in single pass for each element to know
        # that all existing prefix sums (potential k complements) exist
        # before it
        for num in nums:
            currentSum += num

            # check if current number ends subarray(s) summing to k
            kSumComplement = currentSum - k
            if kSumComplement in prefixSumsByFreq:
                subarraySumCount += prefixSumsByFreq[kSumComplement]

            # write sum up to current number as prefix sum for next
            if currentSum not in prefixSumsByFreq:
                prefixSumsByFreq[currentSum] = 0
            prefixSumsByFreq[currentSum] += 1

        return subarraySumCount
