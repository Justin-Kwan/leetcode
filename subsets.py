class Solution:
    # input: [0]
    # output: [[], [0]]
    #
    # input: []
    # output: [[]]
    #
    #               i   
    # input: [1, 1, 1, 1]  curSubset = [1, 1, 1]
    # output: [(), (1), (1, 1), (1, 1, 1), (1, 1, 1, 1)]
    #
    # optimal backtracking approach
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = set([()])
        self.searchSubsets(nums, 0, [], subsets)
        return subsets

    def searchSubsets(self, nums: List[int], nextPos: int, curSubset: List[int], subsets: set[tuple[int, ...]]):
        # at current number, remaining subsets are generated with numbers ahead
        for i in range(nextPos, len(nums)):
            # store set of subsets in tuple form to eliminate disctinct but still
            # duplicate subsets when all input numbers are the same
            curSubset.append(nums[i])
            subsets.add(tuple(curSubset))

            # search and generate all subset combinations on remaining numbers,
            # then backtrack by removing recently added candidate and trying next one
            self.searchSubsets(nums, i + 1, curSubset, subsets)
            curSubset.pop()
