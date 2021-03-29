class Solution:
    # optimal
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allCombos = []
        self.findAllCombosDfs(candidates, [], allCombos, 0, target)
        return allCombos
    
    def findAllCombosDfs(self, candidates: List[int], currCombo: List[int], allCombos: List[List[int]], start: int, target: int):

        if target == 0:
            # currCombo already in sorted order since candidates given in ascending order
            # and we iterate left to right
            allCombos.append(list(currCombo))
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            # try with next candidate in list of sum
            currCombo.append(candidates[i])

            # use current index as starting point for next candidate added recursively to prevent duplicate combos in allCombos
            self.findAllCombosDfs(candidates, currCombo, allCombos, i, target - candidates[i])
            
            # remove current candidate after getting all sum combos with it
            currCombo.pop()
