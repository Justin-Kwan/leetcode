class Solution:
    # optimized bottom up dp memoized
    def numDecodings(self, s: str) -> int:
        totalLetterGroups = 0
        prevLetterGroups = 1
        prevPrevLetterGroups = 1

        for i in range(len(s) - 1, -1, -1):
            # there are 0 letter groups if current digit begins with 0
            totalLetterGroups = 0

            if s[i] != '0':
                totalLetterGroups = prevLetterGroups
                # total groups at current digit is total groups one digit away added
                # to total groups two digits away if within 0 to 26 to unlock other
                # combinations
                if i + 1 < len(s) and int(s[i] + s[i + 1]) <= 26:
                    totalLetterGroups += prevPrevLetterGroups

            prevPrevLetterGroups = prevLetterGroups
            prevLetterGroups = totalLetterGroups

        return totalLetterGroups

    # # optimized top down dp memoized
    # def numDecodings(self, s: str) -> int:
    #     return self.countLetterGroups(s, 0, {})

    # def countLetterGroups(self, s: str, charPos: int, cache: Dict[int, int]) -> int:
    #     # reached end of string
    #     if charPos >= len(s):
    #         return 1
    #     # cannot group digits beginning with 0 to letters
    #     if charPos < len(s) and s[charPos] == '0':
    #         return 0

    #     # return previous computed number of letter groups at current digit
    #     # keyed by position since a digit may occur multiple times in string
    #     if charPos in cache:
    #         return cache[charPos]

    #     # total groups at current digit is total groups one digit away added
    #     # to total groups two digits away if within 0 to 26 to unlock other
    #     # combinations
    #     totalLetterGroups = self.countLetterGroups(s, charPos + 1, cache)
    #     if charPos + 1 < len(s) and int(s[charPos] + s[charPos + 1]) <= 26:
    #         totalLetterGroups += self.countLetterGroups(s, charPos + 2, cache)

    #     cache[charPos] = totalLetterGroups
    #     return totalLetterGroups
