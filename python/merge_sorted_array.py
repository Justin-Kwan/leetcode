class Solution:
    # optimal reverse merge approach
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # take current merged array number as smallest of nums1 and nums2
        pos1, pos2 = m - 1, n - 1

        # merge from end to front by putting largest of nums1 and nums2 at
        # end of merged array
        for i in range(len(nums1) - 1, -1, -1):
            # completed once all numbers from nums2 placed within nums1
            if pos2 < 0:
                break
            # nums1 pointer could go out of range first if nums2 contains a
            # number smaller than smallest in nums1
            if pos1 >= 0 and nums1[pos1] > nums2[pos2]:
                nums1[i] = nums1[pos1]
                pos1 -= 1
            else:
                nums1[i] = nums2[pos2]
                pos2 -= 1

    # # nums1 = [2, 3, 5, 0, 0, 0], m = 3, nums2 = [1, 2, 3]
    # # nums2 = [1, 2, 2, 3, 3, 5], m = 3, nums2 = [-, -, -]
    # #
    # # nums1 = [1, 1, 1, 1, 0, 0, 0] nums2 = [1, 2, 3]
    # # nums2 = [1, 1, 1, 2, 2, 2] nums2 = [-, -, -]
    # #
    # # nums1 = [1, 2, 3, 9, 10, 0, 0, 0] nums2 = [3, 4, 8]
    # # nums2 = [1, 2, 3, 3, 4, 8, 9, 10] nums2 = [-, -, -]
    # #
    # # optimal shifting up approach
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     # shift first m numbers to back to make space for first n numbers from nums2
    #     # (no need to shift 0's to front since will be overwritten anyways)
    #     for i in range(m):
    #         nums1[len(nums1) - i - 1] = nums1[m - i - 1]

    #     # take current merged array number as smallest of nums1 and nums2
    #     pos1, pos2, mergedPos = n, 0, 0
    #     while pos1 < len(nums1) and pos2 < len(nums2):
    #         if nums1[pos1] < nums2[pos2]:
    #             nums1[mergedPos] = nums1[pos1]
    #             pos1 += 1
    #         else:
    #             nums1[mergedPos] = nums2[pos2]
    #             pos2 += 1
    #         mergedPos += 1

    #     # fill in rest of merged array once smaller of nums1 and nums2 exhausted
    #     while pos1 < len(nums1) or pos2 < len(nums2):
    #         if pos1 < len(nums1):
    #             nums1[mergedPos] = nums1[pos1]
    #             pos1 += 1
    #         else:
    #             nums1[mergedPos] = nums2[pos2]
    #             pos2 += 1
    #         mergedPos += 1
