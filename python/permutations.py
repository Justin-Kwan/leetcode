class Solution:
    # using backtracking list (to check which elements are already considered
    # in current permutation or without replacement/duplicates)
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return

        permutationsSoFar = []
        self.searchPermutations(nums, [], permutationsSoFar)
        return permutationsSoFar

    def searchPermutations(self, nums: List[int], currPermutation: List[int], permutationsSoFar: List[int]):
        if len(currPermutation) == len(nums):
            # must copy current permutation since list will be altered when creating other permutations
            permutationsSoFar.append(currPermutation.copy())
            return

        for num in nums:
            if num not in currPermutation:
                currPermutation.append(num)
                self.searchPermutations(
                    nums, currPermutation, permutationsSoFar)
                currPermutation.pop()

    # # using backtracking list (to check which elements are already considered
    # # in current permutation)
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     permutations = self.dfs(nums, [], [])
    #     return permutations

    # def dfs(self, nums: List[int], permutations: List[List[int]], visited: List[int]) -> List[List[int]]:
    #     if len(visited) == len(nums):
    #         permutations.append(visited)    # since visited is a single permutation (branch of tree)
    #         return permutations

        #     for num in nums:                    # cannot alter current list iterated
    #         if num in visited:              # since each number is unique
    #             continue

        #     visited.append(num)             # reduce decision space
    #     newVisited = visited.copy()
    #     permutations = self.dfs(nums, permutations, newVisited)
    #     visited.pop()                   # add back to decision space, can be added in another position if next number takes current position

        # return permutations
