class Solution:
    # optimal hash anagram by letter frequency
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}

        for word in strs:
            # key of anagram group is 26 digits of each char count
            letterFreqs = [0] * 26

            for char in word:
                letterFreqs[ord(char) - ord('a')] += 1

            letterFreqs = tuple(letterFreqs)

            if letterFreqs not in groupedAnagrams:
                groupedAnagrams[letterFreqs] = [word]
            else:
                groupedAnagrams[letterFreqs].append(word)

        return groupedAnagrams.values()


#     # sorted anagram is key
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groupedAnagrams = {}

#         for word in strs:
#             # key of anagram group is the sorted version (unique)
#             sortedWord = ''.join(sorted(word))

#             if sortedWord not in groupedAnagrams:
#                 groupedAnagrams[sortedWord] = [word]
#             else:
#                 groupedAnagrams[sortedWord].append(word)

#         # all grouped anagram lists
#         return groupedAnagrams.values()
