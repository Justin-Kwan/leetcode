class Solution:
    DIGITS_BY_LETTERS = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",            
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }

    # find permutations of N lists using DFS and backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letterCombos = []
        self.searchLetterCombos(digits, 0, "", letterCombos)
        return letterCombos

    def searchLetterCombos(self, digits: str, digitIndex: int, letterCombo: str, letterCombosSoFar: List[str]):
        # add current letter combo when out of range of digits
        if digitIndex >= len(digits):
            letterCombosSoFar.append(letterCombo)
            return

        currDigit = digits[digitIndex]
        digitLetters = self.DIGITS_BY_LETTERS[currDigit]

        # make a new combo with each letter of current digit
        for letter in digitLetters:
            self.searchLetterCombos(digits, digitIndex + 1, letterCombo + letter, letterCombosSoFar)
