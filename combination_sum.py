class Solution:
    # optimal dfs
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comboSums = []
        self.findAllCombinations(candidates, 0, target, [], comboSums)
        return comboSums

    def findAllCombinations(self, candidates: List[int], start: int, target: int, currCombo: List[int], comboSums: List[int]):
        if target < 0:
            return
        if target == 0:
            # current combo is always unique and sorted since candidates
            # is always sorted in ascending order
            comboSums.append(currCombo.copy())
            return

        # since all numbers are unique, avoid duplicate combos by
        # skipping all previously "fixed" numbers for future combos
        for i in range(start, len(candidates)):
            # try permutation with current num
            currCombo.append(candidates[i])

            self.findAllCombinations(candidates, i, target - candidates[i], currCombo, comboSums)

            # remove current num to try next num in combo
            currCombo.pop()
