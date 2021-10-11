class Solution:
    # optimal
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagramsLookup = {}
        groupedAnagrams = []

        # dump words into map
        for word in strs:
            anagramKey = "".join(sorted(word))

            if anagramKey not in groupedAnagramsLookup:
                groupedAnagramsLookup[anagramKey] = [word]
            else:
                groupedAnagramsLookup[anagramKey].append(word)

        # flatten map to get all lists
        for anagramKey in groupedAnagramsLookup:
            groupedAnagrams.append(groupedAnagramsLookup[anagramKey])

        return groupedAnagrams
