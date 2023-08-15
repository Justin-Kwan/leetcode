class Solution:
    # top down dp approach
    def wordBreak(self, input: str, wordDict: List[str]) -> List[str]:
        wordPath = self.buildSentences(input, set(wordDict), {}, 0)
        return [" ".join(words) for words in wordPath]

    def buildSentences(self, input: str, words: Set[str], cache: Dict[int, List[str]], curPos: int) -> List[List[str]]:
        # reached end of input after final word in sentence
        if curPos >= len(input):
            return [[]]
        # revisiting character, immediately return result of path or
        # empty flat list if no sentence path from current character
        if curPos in cache:
            return cache[curPos]

        # cached word path from current character begins as empty
        cache[curPos] = []

        # explore all prefixes from current character
        for i in range(curPos, len(input)):
            curPrefix = input[curPos : i + 1]
            if curPrefix not in words:
                continue

            # prepend current prefix as part of sentence path starting
            # from next character (may be empty if no paths onward)
            for wordPath in self.buildSentences(input, words, cache, i + 1):
                cache[curPos].append([curPrefix] + wordPath)

        return cache[curPos]
