class Solution:
    # bottom up dp approach
    def wordBreak(self, input: str, wordDict: List[str]) -> List[str]:
        dictionary = set(wordDict)
        prefixPaths = []

        # every path is stored in matrix at index after last character for
        # ease of access for next word in path
        for i in range(len(input) + 1):
            # first word of path must be appended to empty string at 0th index
            emptyWordPath = [""] if i == 0 else []
            prefixPaths.append(emptyWordPath)

        # iterate through every substring in input, ending at each character
        # skip first entry since paths are only stored >= index 1
        for endPos in range(1, len(input) + 1):
            for startPos in range(0, endPos):
                curPrefix = input[startPos : endPos]
                if curPrefix in dictionary:
                    # append current word to prefix paths, path may be empty
                    # at current index if no path leads to current word
                    for wordPath in prefixPaths[startPos]:
                        curWordPath = curPrefix if not wordPath else wordPath + " " + curPrefix
                        prefixPaths[endPos].append(curWordPath)

        # only return paths that reach last character in string (end position)
        return prefixPaths[len(input)]

    # # optimized bottom up dp approach
    # def wordBreak(self, input: str, wordDict: List[str]) -> List[str]:
    #     dictionary = set(wordDict)
    #     prefixPaths = []
    #     for i in range(len(input) + 1):
    #         # first words of paths (end positions) must be appended to empty
    #         # initialized path in 0th index
    #         emptyWordBreak = [[0]] if i == 0 else []
    #         prefixPaths.append(emptyWordBreak)

    #     # iterate through every substring in input, ending at each character
    #     # skip first entry end position since paths can only be stored at or
    #     # after index 1
    #     for endPos in range(1, len(input) + 1):
    #         for startPos in range(0, endPos):
    #             if input[startPos : endPos] in dictionary:
    #                 # append current word to prefix path using only its start
    #                 # and end positions to save space, word breaks path may be
    #                 # empty at current index if no path leads to current word
    #                 for wordBreaks in prefixPaths[startPos]:
    #                     prefixPaths[endPos].append(wordBreaks + [endPos])

    #     # reconstruct full word path sentences from indices of word breaks
    #     finalPaths = []
    #     for wordBreaks in prefixPaths[len(input)]:
    #         wordPath = []
    #         for i in range(len(wordBreaks) - 1):
    #             wordPath.append(input[wordBreaks[i] : wordBreaks[i + 1]])
    #         finalPaths.append(" ".join(wordPath))

    #     return finalPaths

    # # optimal top down dp approach
    # def wordBreak(self, input: str, wordDict: List[str]) -> List[str]:
    #     wordPath = self.buildSentences(input, set(wordDict), {}, 0)
    #     return [" ".join(words) for words in wordPath]

    # def buildSentences(self, input: str, words: Set[str], cache: Dict[int, List[str]], curPos: int) -> List[List[str]]:
    #     # reached end of input after final word in sentence
    #     if curPos >= len(input):
    #         return [[]]
    #     # revisiting character, immediately return result of path or
    #     # empty flat list if no sentence path from current character
    #     if curPos in cache:
    #         return cache[curPos]

    #     # cached word path from current character begins as empty
    #     cache[curPos] = []

    #     # explore all prefixes from current character
    #     for i in range(curPos, len(input)):
    #         curPrefix = input[curPos : i + 1]
    #         if curPrefix not in words:
    #             continue

    #         # prepend current prefix as part of sentence path starting
    #         # from next character (may be empty if no paths onward)
    #         for wordPath in self.buildSentences(input, words, cache, i + 1):
    #             cache[curPos].append([curPrefix] + wordPath)

    #     return cache[curPos]
