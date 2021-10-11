class Solution:
#     # swapping approach
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         leftPtr = 0
#         rightPtr = 0
        
#         while rightPtr < len(nums) and leftPtr < len(nums):

#             # swap case
#             if nums[leftPtr] == 0 and nums[rightPtr] != 0 and leftPtr < rightPtr:
#                 tempNumAtLeftPtr = nums[leftPtr]
#                 nums[leftPtr] = nums[rightPtr]
#                 nums[rightPtr] = tempNumAtLeftPtr
#                 rightPtr += 1
#             # case when leftPtr = 0 and rightPtr = 0 or rightPtr < leftPtr
#             elif nums[leftPtr] == 0:
#                 rightPtr += 1
#             else:
#                 leftPtr += 1

    # throw back to front approach
    def moveZeroes(self, nums: List[int]) -> None:
        leftPtr = 0
        
        # right ptr searches for next non 0 number, left ptr will be replaced, and left ptr will move up by one each time
        for num in nums:
            if num != 0:
                nums[leftPtr] = num
                leftPtr += 1

        # remaining numbers that were "thrown" to left ptr but left in their original position are cleaned up to 0s
        while leftPtr < len(nums):
            nums[leftPtr] = 0
            leftPtr += 1

