class Solution:

    # brute force
    # handle empty list case
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currentLongest = ""
        
        if len(strs) == 0:
            return currentLongest

        # match chars in shortest word with all words in strs
        for i in range(0, len(strs[0])):

            # check each word in strs has same char at pos i
            for word in strs:
                
                # if chars don't match or char in curr word doesn't exist (word is smaller)
                # check range of word before accessing ith char of word
                if i > len(word) - 1 or word[i] != strs[0][i]:
                    return currentLongest

            currentLongest += strs[0][i]

        return currentLongest


# test cases:
# assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
# assert longestCommonPrefix(["flower","flow", "fp", "flight"]) == "f"
# assert longestCommonPrefix(["flower","flow", "g", "flight"]) == ""
# assert longestCommonPrefix(["flower","flow", "", "flight"]) == ""
# assert longestCommonPrefix(["dog","racecar","car"]) == ""
# assert longestCommonPrefix(["hello"]) == "hello"
# assert longestCommonPrefix([]) == ""
