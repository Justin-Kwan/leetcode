class Solution:
    # optimal hashmap, check behind
    def subarraySum(self, nums: List[int], k: int) -> int:
        # account for case when first element = k (its own subarray)
        sumsByCount = { 0: 1 }
        sumUpToCurr, subarrayCount = 0, 0

        for num in nums:
            sumUpToCurr += num

            # first check if k sum complement exists as sum previously
            # before adding current to prevent counting (curr - curr) if k = 0
            if sumUpToCurr - k in sumsByCount:
                subarrayCount += sumsByCount[sumUpToCurr - k]

            # write sum up to current in map for use by later sum
            if sumUpToCurr not in sumsByCount:
                sumsByCount[sumUpToCurr] = 1
            else:
                sumsByCount[sumUpToCurr] += 1

        return subarrayCount
