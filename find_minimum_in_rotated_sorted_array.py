class Solution:
    #  L                       R
    # [3, 4, 5, 6, 7, 8, 9, 1, 2]
    #  L                       R
    # [9, 1, 2, 3, 4, 5, 6, 7, 8]
    def findMin(self, nums: List[int]) -> int:
        lastIndex = len(nums) - 1
        
        # hadle case of non-rotated list
        if nums[0] < nums[lastIndex]:
            return nums[0]

        leftPtr = 0
        rightPtr = len(nums) - 1

        while leftPtr < rightPtr:
            midPtr = (leftPtr + rightPtr) // 2

            # middle value is left of decrease (on left sequence)
            if nums[midPtr] >= nums[0]:
                leftPtr = midPtr + 1

            # middle value is right of decrease (on right sequence)
            if nums[midPtr] < nums[lastIndex]:
                rightPtr = midPtr

        return nums[leftPtr]
