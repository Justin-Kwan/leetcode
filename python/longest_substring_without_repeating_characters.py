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

            seenChars = set()
            maxUniqueLength = 0

            while rightPtr < len(s):
                if s[rightPtr] not in seenChars:
                    seenChars.add(s[rightPtr])
                    rightPtr += 1
                else:
                    seenChars.remove(s[leftPtr])
                    leftPtr += 1

                # unique subtring is in valid state now
                maxUniqueLength = max(maxUniqueLength, len(seenChars))

            return maxUniqueLength
