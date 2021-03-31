class Solution:
    # using backtracking list (to check which elements are already considered 
    # in current permutation)
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = self.dfs(nums, [], [])
        return permutations
        
    def dfs(self, nums: List[int], permutations: List[List[int]], visited: List[int]) -> List[List[int]]:
        if len(visited) == len(nums):
            permutations.append(visited)    # since visited is a single permutation (branch of tree)
            return permutations
        
	    for num in nums:                    # cannot alter current list iterated
            if num in visited:              # since each number is unique
                continue
            
	    visited.append(num)             # reduce decision space
        newVisited = visited.copy()
        permutations = self.dfs(nums, permutations, newVisited)
        visited.pop()                   # add back to decision space, can be added in another position if next number takes current position

	return permutations
