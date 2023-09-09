class Solution:
    # stack approach
    def decodeString(self, encoded: str) -> str:
        encodedCharStack = []

        for i in range(len(encoded)):
            # decode current nested subexpression
            if encoded[i] == ']':
                decodedExpression, expressionCount = "", ""
                # parse expression letters between brackets, prepend
                while encodedCharStack[-1] != '[':
                    decodedExpression = encodedCharStack.pop() + decodedExpression

                # discard opening bracket to current expression
                encodedCharStack.pop()

                # parse expression count preceding opening bracket, prepend
                while encodedCharStack and encodedCharStack[-1].isdigit():
                    expressionCount = encodedCharStack.pop() + expressionCount

                # put decoded expression back onto stack to be processed as
                # part of potential outer surrounding expression
                encodedCharStack.append(
                    decodedExpression * int(expressionCount))
            else:
                encodedCharStack.append(encoded[i])

        # stack now contains one or more decoded expressions k[a-z], a-z from
        # root expression
        return "".join(encodedCharStack)

    # # optimal recursive walking approach
    # def decodeString(self, encoded: str) -> str:
    #     if not encoded:
    #         return ""

    #     curPos, decodedChars = 0, []

    #     # keep parsing each expression "k[...]" or "a-z" at root layer
    #     while curPos < len(encoded):
    #         curPos = self.parseExpression(encoded, curPos, decodedChars)
    #         curPos += 1

    #     return "".join(decodedChars)

    # def parseExpression(self, encoded: str, curPos: int, decodedChars: List[str]) -> int:
    #     # parse leading integer denoting expression repititions
    #     countStartPos = curPos
    #     while encoded[curPos].isdigit():
    #         curPos += 1

    #     # expression count defaults to 1 if no leading integer
    #     expressionCount = 1 if countStartPos == curPos else int(encoded[countStartPos:curPos])
    #     oldDecodedLen = len(decodedChars)

    #     # parse letters and subexpressions in current expression from '['
    #     while curPos < len(encoded) and encoded[curPos] != ']':
    #         # recursively walk and parse subexpression, jump to new position
    #         if encoded[curPos].isdigit():
    #             curPos = self.parseExpression(encoded, curPos, decodedChars)
    #         elif encoded[curPos].isalpha():
    #             decodedChars.append(encoded[curPos])

    #         # skip the ']' of inner subexpression to prevent exiting current
    #         # expression too early
    #         curPos += 1

    #     # duplicate and append the already parsed expression, avoid recomputing
    #     parsedExpression = decodedChars[oldDecodedLen:]
    #     decodedChars.extend(parsedExpression * (expressionCount - 1))

    #     # now at closing ']' of current expression
    #     return curPos

    # # simplified recursive approach
    # def decodeString(self, encoded: str) -> str:
    #     if not encoded:
    #         return ""

    #     decoded, _ = self.parseExpression(encoded, 0)
    #     return decoded

    # def parseExpression(self, encoded: str, curPos: int):
    #     # expression count defaults to 1 if no leading integer
    #     expressionCount = 0
    #     curDecoded = ""

    #     # parse letters and subexpressions in current expression from '['
    #     while curPos < len(encoded):
    #         if encoded[curPos].isdigit():
    #             expressionCount = (expressionCount * 10) + int(encoded[curPos])
    #         # parse subexpression and jump to new position
    #         elif encoded[curPos] == '[':
    #             subDecoded, curPos = self.parseExpression(encoded, curPos + 1)
    #             # duplicate already parsed expression, avoid recomputing
    #             curDecoded += subDecoded * expressionCount
    #             expressionCount = 0
    #         # now at closing ']' of current expression
    #         elif encoded[curPos] == ']':
    #             return curDecoded, curPos
    #         else:
    #             curDecoded += encoded[curPos]

    #         # skip the ']' of inner subexpression to prevent exiting current
    #         # expression too early
    #         curPos += 1

    #     # completed parsing expression "a-z" without brackets
    #     return curDecoded, curPos
