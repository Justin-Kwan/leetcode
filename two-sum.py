class Solution:
    # returns two indices whose elements sum to target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsLookup = {}
        
        # dump array into hashmap
        for i in range(len(nums)):
            numsLookup[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in numsLookup and numsLookup[complement] != i:
                return [ numsLookup[complement], i ]
