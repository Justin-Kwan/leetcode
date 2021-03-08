class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(nums) - 1
        
        while leftPtr < rightPtr:
            centerPtr = (rightPtr + leftPtr) // 2
            
            if nums[centerPtr] < nums[rightPtr]:
                rightPtr = centerPtr
            elif nums[centerPtr] >= nums[leftPtr]:
                leftPtr = centerPtr + 1 # assuming that there is 1 rotated element to the right

        return nums[rightPtr]
