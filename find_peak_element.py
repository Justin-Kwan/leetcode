class Solution:
    # optimal binary search
    def findPeakElement(self, nums: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(nums) - 1

        while leftPtr < rightPtr:
            # center pointer can never go out of range (< 0 or > length)
            centerPtr = (leftPtr + rightPtr) // 2

            # center pointer at local peak
            if nums[centerPtr - 1] < nums[centerPtr] and nums[centerPtr] > nums[centerPtr + 1]:
                return centerPtr
            # move right if right number larger (peak on right)
            if nums[centerPtr] < nums[centerPtr + 1]:
                leftPtr = centerPtr + 1
            # move left if left number larger (peak on left)
            elif nums[centerPtr - 1] > nums[centerPtr]:
                rightPtr = centerPtr - 1           

        return leftPtr
