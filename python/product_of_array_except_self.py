class Solution:
    # optimized left products then overlay right products
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productsExceptSelf = [0] * len(nums)

        # calculate and store left products
        for i in range(0, len(nums)):
            if i == 0:              # left product of first is 1
                productsExceptSelf[i] = 1
            else:
                productsExceptSelf[i] = nums[i - 1] * productsExceptSelf[i - 1]

        rightProduct = 1

        # calculate and overlay right products
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:   # right product of last is 1
                rightProduct = nums[i + 1] * rightProduct

            productsExceptSelf[i] *= rightProduct

        return productsExceptSelf


#     # unoptimized left right product lists
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         numCount = len(nums)

#         leftProducts = [0] * numCount     # left product up to each element
#         rightProducts = [0] * numCount    # right product up to each element

#         # calculate and store products
#         left, right = 0, numCount - 1     

#         while left < numCount:
#             # product to left of first element always 1
#             if left == 0:
#                 leftProducts[left] = 1
#             # left product up to current element is previous * left product up to it
#             else:
#                 leftProducts[left] = nums[left - 1] * leftProducts[left - 1]

#             # product to right of last element always 1
#             if right == numCount - 1:
#                 rightProducts[right] = 1
#             # right product up to current element is previous * right product up to it
#             else:
#                 rightProducts[right] = nums[right + 1] * rightProducts[right + 1]

#             left += 1
#             right -= 1

#         for i in range(0, numCount):
#             nums[i] = leftProducts[i] * rightProducts[i]

#         return nums
