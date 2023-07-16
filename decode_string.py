class Solution:
    # recursive char walking approach
    def decodeString(self, encoded: str) -> str:
        if not encoded:
            return ""

        curPos, decodedChars = 0, []

        # keep parsing each expression "k[...]" or "a-z" at root layer
        while curPos < len(encoded):
            curPos = self.parseExpression(encoded, curPos, decodedChars)
            curPos += 1

        return "".join(decodedChars)

    def parseExpression(self, encoded: str, curPos: int, decodedChars: List[str]) -> int:
        # parse leading integer denoting expression repititions
        countStartPos = curPos
        while encoded[curPos].isdigit():
            curPos += 1

        # expression count defaults to 1 if no leading integer
        expressionCount = 1 if countStartPos == curPos else int(
            encoded[countStartPos:curPos])
        oldDecodedLen = len(decodedChars)

        # parse letters and subexpressions in current expression from '['
        while curPos < len(encoded) and encoded[curPos] != ']':
            # recursively walk and parse subexpression, jump to new position
            if encoded[curPos].isnumeric():
                curPos = self.parseExpression(encoded, curPos, decodedChars)
            elif encoded[curPos].isalpha():
                decodedChars.append(encoded[curPos])

            # skip the ']' of inner subexpression to prevent exiting current
            # expression too early
            curPos += 1

        # duplicate and append the already parsed expression, avoid recomputing
        parsedExpression = decodedChars[oldDecodedLen:]
        decodedChars.extend(parsedExpression * (expressionCount - 1))

        # now at closing ']' of current expression
        return curPos
