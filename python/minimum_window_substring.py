class Solution:
    # optimal two pointers approach
    def minWindow(self, s: str, t: str) -> str:
        # build freqency map of letters in t for each window to compare with
        totalLetters, letterFreqs = 0, defaultdict(int)
        for letter in t:
            totalLetters += 1
            letterFreqs[letter] += 1
 
        minWindowSize, minWindowRange = float('inf'), (-1, -1)
        totalWindowLetters, windowLetterFreqs = 0, dict.fromkeys(letterFreqs, 0)

        # right pointer always ahead of window by 1 so left pointer can
        # clear all letters in window without being stuck at a last one
        # in t preventing right from expanding again
        leftPos = rightPos = 0
        while rightPos < len(s):
            # expand current window to search if missing some letters from t
            if totalWindowLetters < totalLetters:
                rightPos += 1
                rightLetter = s[rightPos - 1]  

                # increment new letter from t added to current window
                if rightLetter in letterFreqs:
                    # redundant letters from t inside window do not contribute
                    if windowLetterFreqs[rightLetter] < letterFreqs[rightLetter]:
                        totalWindowLetters += 1
                    windowLetterFreqs[rightLetter] += 1

            # contract current window once it contains all letters from t
            while totalWindowLetters >= totalLetters:
                leftLetter = s[leftPos]
                # check if current valid window is smallest seen
                if rightPos - leftPos < minWindowSize:
                    minWindowSize = rightPos - leftPos
                    minWindowRange = (leftPos, rightPos)

                # decrement letter from t at end of current window
                if leftLetter in letterFreqs:
                    # redundant letters from t inside window do not contribute
                    if windowLetterFreqs[leftLetter] <= letterFreqs[leftLetter]:
                        totalWindowLetters -= 1
                    windowLetterFreqs[leftLetter] -= 1

                leftPos += 1

        return s[minWindowRange[0] : minWindowRange[1]]

    # # suboptimal lookahead approach
    # def minWindow(self, s: str, t: str) -> str:
    #     if len(t) > len(s):
    #         return ""

    #     minWindowSize, minPos = float('inf'), [0, 0]
    #     letterFreqs = defaultdict(int)

    #     for char in t:
    #         letterFreqs[char] += 1

    #     for i in range(len(s)):
    #         if s[i] not in letterFreqs:
    #             continue

    #         seenLetterFreqs = letterFreqs.copy()
    #         j = i

    #         while seenLetterFreqs and j < len(s) and ((j-1) - i) < minWindowSize:
    #             if s[j] in seenLetterFreqs:
    #                 seenLetterFreqs[s[j]] -= 1
    #                 if seenLetterFreqs[s[j]] <= 0:
    #                     del seenLetterFreqs[s[j]]
    #             j += 1

    #         if not seenLetterFreqs and (j - i) < minWindowSize:
    #             minWindowSize, minPos = j - i, [i, j]

    #     return s[minPos[0] : minPos[1]]
