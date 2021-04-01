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

    # optimal backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        generatedParenthesis = []
        self.recurseGenerateParenthesis('(', generatedParenthesis, 1, 0, n)
        return generatedParenthesis
    
    def recurseGenerateParenthesis(self, parenthesisSoFar: str, generatedParenthesis: List[str], leftCount: int, rightCount: int, n: int):

        if leftCount == n and rightCount == n:
            generatedParenthesis.append(parenthesisSoFar)
            return
        
        # check enough left bracket to accomodate new right bracket
        if leftCount > rightCount:
            self.recurseGenerateParenthesis(parenthesisSoFar + ')', generatedParenthesis, leftCount, rightCount + 1, n)

        # check not all left bracket used before adding new left bracket
        if leftCount < n:
            self.recurseGenerateParenthesis(parenthesisSoFar + '(', generatedParenthesis, leftCount + 1, rightCount, n)

