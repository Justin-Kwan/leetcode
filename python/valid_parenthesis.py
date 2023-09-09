class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        bracketMap = {
            "(": ")",
            "{": "}",
            "[": "]" 
        }
        
        for currBracket in s:
            isOpeningBracket = currBracket in bracketMap

            if isOpeningBracket:
                brackets.append(currBracket) 
            else:
                if len(brackets) == 0 or bracketMap[brackets.pop()] != currBracket:
                    return False

        # could be extra remaining closing brackets
        areNoBracketsLeft = len(brackets) == 0

        return areNoBracketsLeft


# test cases

# consider:
#   - when closing bracket does not match opening bracket
#   - when extra closing brackets at end (don't pop empty stack)
#   - when not enough closing brackets (remaining opening brackets in stack at end)

# (){}[]
# ({[]}[]())
        
# ([)]
# [ (  ]  [
        
# [( also invalid
# }}}}}}}}}}}}}}}} also invalid (edge case, pop only if len(stack) >= 1)

