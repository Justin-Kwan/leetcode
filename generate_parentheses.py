class Solution:
#     # brute force
#     def generateParenthesis(self, n: int) -> List[str]:
#         generatedParenthesis = []
#         self.recurseGenerateParenthesis('', n, generatedParenthesis)
#         return generatedParenthesis

#     def recurseGenerateParenthesis(self, parenthesisSoFar: str, openingBracketCount: int, generatedParenthesis: List[str]):
        
#         if len(parenthesisSoFar) == openingBracketCount * 2:
#             if self.isValidParenthesis(parenthesisSoFar):
#                 generatedParenthesis.append(parenthesisSoFar)

#             return
                
#         # explore if adding '(' to parenthesis so far
#         self.recurseGenerateParenthesis(parenthesisSoFar + '(', openingBracketCount, generatedParenthesis)
        
#         # explore if adding ')' to parenthesis so far
#         self.recurseGenerateParenthesis(parenthesisSoFar + ')', openingBracketCount, generatedParenthesis)
        
#     def isValidParenthesis(self, parenthesis: str):
#         openingBracketCount = 0
        
#         for bracket in parenthesis:
#             if bracket == '(':
#                 openingBracketCount += 1
#             else:
#                 openingBracketCount -= 1
                
#                 # when too many closing brackets
#                 if openingBracketCount < 0:
#                     return False
        
#         # when too many opening brackets
#         return openingBracketCount == 0

    # optimal dfs
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesisCombos = []
        self.generateParenthesisCombos("", n, n, parenthesisCombos)
        return parenthesisCombos

    def generateParenthesisCombos(self, currCombo: str, openingLeft: int, closingLeft: int, combos: List[str]):        
        # reached valid parenthesis permutation
        if openingLeft == 0 and closingLeft == 0:
            combos.append(currCombo)
            return

        # can explore by opening a new parenthesis
        if openingLeft > 0:
            self.generateParenthesisCombos(currCombo + '(',
                                           openingLeft - 1,
                                           closingLeft,
                                           combos)

        # check that a closing parenthesis can accomodate an opening one
        if closingLeft > openingLeft:
            self.generateParenthesisCombos(currCombo + ')',
                                           openingLeft,
                                           closingLeft - 1,
                                           combos)  
