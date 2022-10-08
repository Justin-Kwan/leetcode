class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dump all numbers by position into hashmap
        numsByPos = {}
        for i in range(len(nums)):
            # intentionally overwrite previous duplicate number's position to indicate both 
            # are not the same element
            numsByPos[nums[i]] = i

        # find a possible complement of each number to sum to target
        for i in range(len(nums)):
            complement = target - nums[i]

            # complement of number exists and check both are not the same element
            # (complement should be ahead of current number for unique or duplicate pairs)
            if complement in numsByPos and i < numsByPos[complement]:
                return [i, numsByPos[complement]]
