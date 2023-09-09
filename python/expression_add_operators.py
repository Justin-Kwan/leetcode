class Solution:
    # simplified optimal backtracking approach
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []

        matchingExpressions = []

        def searchExpressions(termStartPos: int, curPath: str, curTotal: int, lastTermApplied: int):
            # reached leaf node of last term in expression, add expressions that
            # yield target value
            if termStartPos >= len(num):
                if curTotal == target:
                    matchingExpressions.append(curPath)
                return

            # consider all possible next terms in expression of all digit lengths
            for termEndPos in range(termStartPos, len(num)):
                # ignore any terms with a leading 0 expect for 0 itself, all
                # remaining nodes on same level lead with 0 so prune
                if num[termStartPos] == '0' and termStartPos < termEndPos:
                    return

                nextTerm = int(num[termStartPos : termEndPos + 1])

                # all possible first terms cannot be prefixed or applied with math
                # operation, recurse with it as total so far
                if termStartPos == 0:
                    searchExpressions(termEndPos + 1, str(nextTerm), nextTerm, nextTerm)
                    continue

                # preemptively add, subtract and multiply current total against next term
                searchExpressions(termEndPos + 1, curPath + '+' + str(nextTerm), curTotal + nextTerm, nextTerm)
                searchExpressions(termEndPos + 1, curPath + '-' + str(nextTerm), curTotal - nextTerm, -nextTerm)
                # fix incorrectly applied +/- from product term by undoing multiplication,
                # recomputing and extending the product against the next term to multiply
                # with, and reapply by adding back to total
                correctedTotal = (curTotal - lastTermApplied) + (lastTermApplied * nextTerm)
                extendedProduct = lastTermApplied * nextTerm
                searchExpressions(termEndPos + 1, curPath + '*' + str(nextTerm), correctedTotal, extendedProduct)

        searchExpressions(0, "", 0, 0)
        return matchingExpressions

    # # optimal backtracking approach
    # def addOperators(self, num: str, target: int) -> List[str]:
    #     if not num:
    #         return []

    #     matchingExpressions = []

    #     def searchExpressions(termStartPos: int, curPath: List[str], curTotal: int, lastTermApplied: int):
    #         # reached leaf node of last term in expression
    #         if termStartPos >= len(num):
    #             # add expressions that yield target value
    #             if curTotal == target:
    #                 matchingExpressions.append(''.join(curPath))
    #             return

    #         # consider all possible next terms in expression of all digit lengths
    #         for termEndPos in range(termStartPos, len(num)):
    #             # ignore any terms with a leading 0 expect for 0 itself, all
    #             # remaining nodes on same level lead with 0 so prune
    #             if num[termStartPos] == '0' and termStartPos < termEndPos:
    #                 return

    #             nextTerm = int(num[termStartPos : termEndPos + 1])

    #             # all possible first terms cannot be prefixed or applied with math
    #             # operation, recurse with it as total so far
    #             if termStartPos == 0:
    #                 searchExpressions(termEndPos + 1, [str(nextTerm)], nextTerm, nextTerm)
    #                 continue

    #             # preemptively add, subtract and multiply current total against next term
    #             for operator in ['*', '+', '-']:
    #                 curPath.append(operator + str(nextTerm))

    #                 if operator == '+':
    #                     searchExpressions(termEndPos + 1, curPath, curTotal + nextTerm, nextTerm)
    #                 elif operator == '-':
    #                     searchExpressions(termEndPos + 1, curPath, curTotal - nextTerm, -nextTerm)
    #                 else:
    #                     # fix the incorrectly applied +/- from product term by undoing the
    #                     # multiplication, recomputing and extending the product against the
    #                     # next term to multiply with, and reapply by adding back to total
    #                     correctedTotal = (curTotal - lastTermApplied) + (lastTermApplied * nextTerm)
    #                     extendedProduct = lastTermApplied * nextTerm
    #                     searchExpressions(termEndPos + 1, curPath, correctedTotal, extendedProduct)

    #                 curPath.pop()

    #     searchExpressions(0, [], 0, 0)
    #     return matchingExpressions
