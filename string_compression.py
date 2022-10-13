class Solution:
    # test cases:
    #                              r
    #                           l
    # ["a","2","b","2","c","3","c"] -> 6
    # curChar = None, runLength = 3
    #                                  r
    #                           l
    # ["a","4","b","4","c","1","b","c"] -> 6
    # curChar = None, runLength = 1
    #          r
    #          l
    # ["a","2"] -> 2
    # curChar = None, runLength = 2
    #      r
    #      l
    # ["a"] -> 1
    # curChar = None, runLength = 0
    #              r
    #              l
    # ["a","b","c"] -> 3
    # curChar = None, runLength = 1
    #
    # optimal two pointers approach
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        leftPos = rightPos = 0
        curChar, runLength = chars[0], 0

        # current character no longer exists after run length is written
        # for final character group
        while curChar:
            if rightPos < len(chars) and chars[rightPos] == curChar:
                runLength += 1
                rightPos += 1
                continue

            # right pointer found a new character group or reached end, write
            # previous character and it's length
            chars[leftPos] = curChar
            leftPos += 1

            # write all digits of group's run length in subsequent indices
            if runLength > 1:
                for digit in str(runLength):
                    chars[leftPos] = digit
                    leftPos += 1

            # update to new group's character at right pointer with empty
            # run length, or null if right pointer reached end
            curChar = chars[rightPos] if rightPos < len(chars) else None
            runLength = 0

        return leftPos
