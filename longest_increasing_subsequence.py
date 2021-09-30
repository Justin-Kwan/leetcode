class Solution:
    # unoptimized bottom up DP
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # first num has subsequence of size 1
        LISUpToNums = [1]
        maxLIS = 1

        for i in range(1, len(nums)):
            # max LIS up to current = LIST of number < current in left sublist
            LISUpToCurr = self.findLISBefore(nums[i], 0, i, nums, LISUpToNums) + 1

            LISUpToNums.append(LISUpToCurr)
            maxLIS = max(maxLIS, LISUpToCurr)

        return maxLIS
    
    # finds LIS out of all elements to left of currNum at toIndex and less than currNum
    # (for currNum to succeed in increasing sequence)
    def findLISBefore(self, currNum: int, fromIndex: int, toIndex: int, nums: List[int], LISUpToNums: List[int]) -> int:
        # non empty sublist has at least 1 subsequence
        maxLISBeforeCurr = 0
        
        for i in range(fromIndex, toIndex):
            # replace with element < current with larger LIS up to it
            if nums[i] < currNum:
                maxLISBeforeCurr = max(maxLISBeforeCurr, LISUpToNums[i])

        return maxLISBeforeCurr
