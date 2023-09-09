class Solution:
    # optimal binary search approach
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find first occurrence of target (lower bound position)
        lowerBoundPos = self.findTargetBound(nums, target, -1)
        # find last occurrence target (upper bound position)
        upperBoundPos = self.findTargetBound(nums, target, 1)

        return [lowerBoundPos, upperBoundPos]

    def findTargetBound(self, nums: List[int], target: int, direction: int) -> int:
        leftPos, rightPos = 0, len(nums) - 1

        while leftPos <= rightPos:
            middlePos = (leftPos + rightPos) // 2

            if target > nums[middlePos]:
                leftPos = middlePos + 1

            elif target < nums[middlePos]:
                rightPos = middlePos - 1

            # once target is found, if target also exists to left, continue to left
            # if target also exists to right, continue to right
            elif (nums[middlePos] == target and
                middlePos + direction >= 0 and middlePos + direction < len(nums) and
                nums[middlePos + direction] == target):

                # continue searching in left or right for first or last occurrence
                # depending on given direction (-1 or +1)
                if direction == -1:
                    rightPos = middlePos + direction
                else:
                    leftPos = middlePos + direction

            # found only single occurrence of target
            else:
                return middlePos

        return -1
