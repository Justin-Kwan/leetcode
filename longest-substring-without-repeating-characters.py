class Solution:
#     # brute force
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seenChars = set()
#         largestUniqueSoFar = 0 

#         for i in range(0, len(s)):
#             largestSubstring = 0

#             for j in range(i, len(s)):
#                 if s[j] not in seenChars:
#                     seenChars.add(s[j])
#                 else:
#                     break

#             seenChars.clear()

#             if largestSubstring > largestUniqueSoFar:
#                 largestUniqueSoFar = largestSubstring

#         return largestUniqueSoFar
    
    # optomized
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPtr = 0
        rightPtr = 0

        largestUniqueSoFar = 0
        currUniqueChars = set()
        
        while rightPtr < len(s):

            if s[rightPtr] not in currUniqueChars:
                currUniqueChars.add(s[rightPtr])
                rightPtr += 1
            else:
                currUniqueChars.remove(s[leftPtr])
                leftPtr += 1

            if len(currUniqueChars) > largestUniqueSoFar:
                largestUniqueSoFar = len(currUniqueChars)
        
        return largestUniqueSoFar
        
    
