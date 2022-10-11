class Solution:
    #                    
    # [-4,+3,+2,-7,8,2,-3,-1],
    # [2, 3]
    #
    # optimal modify index approach
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicateNums = []

        # go through all numbers and mark as seen in corresponding index, only
        # works because each number in list have a valid index and there are no
        # negative numbers
        # (ex. number repeated thrice looks same as number repeated once)
        for num in nums:
            # another number may have negated current one
            numIndex = abs(num) - 1

            # positive means seen for first time, mark as seen
            if nums[numIndex] > 0:
                nums[numIndex] *= -1
            # negative means second time seeing current number
            else:
                duplicateNums.append(abs(num))

        return duplicateNums
