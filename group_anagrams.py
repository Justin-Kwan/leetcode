class Solution:
    # optimal anagram's letter count is key
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}

        for word in strs:
            # key of anagram group is 26 digits of each char count
            charCount = [0] * 26

            for char in word:
                charCount[ord(char) - ord('a')] += 1

            if tuple(charCount) not in groupedAnagrams:
                groupedAnagrams[tuple(charCount)] = [word]
            else:
                groupedAnagrams[tuple(charCount)].append(word)

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
