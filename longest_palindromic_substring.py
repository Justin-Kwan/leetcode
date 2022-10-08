class Solution:
    # input: "a"
    # output: "a"
    # longest range = (0, 0)
    #
    # input: "babad"
    # output: "bab"
    # longest range = (0, 2)
    #
    # input: "cabzbaabd"
    # ouptut: "abzba"
    # longest range = (1, 5)

#     # expand from single or adjacent characters approach
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""

#         longestPalindromeRange = (0, 0)

#         # expand from middle of single or two adjacent characters, to left and right
#         for i in range(1, len(s)):
#             # expand from current single character
#             left = right = i
#             while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
#                 palindromeLength = (right - left) + 1
#                 longestPalindromeLength = (longestPalindromeRange[1] - longestPalindromeRange[0]) + 1

#                 # update longest palindrome range seen
#                 if palindromeLength > longestPalindromeLength:
#                     longestPalindromeRange = (left, right)

#                 left -= 1
#                 right += 1

#             # expand from current and previous adjacent character
#             left, right = i - 1, i
#             while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
#                 palindromeLength = (right - left) + 1
#                 longestPalindromeLength = (longestPalindromeRange[1] - longestPalindromeRange[0]) + 1

#                 # update longest palindrome range seen
#                 if palindromeLength > longestPalindromeLength:
#                     longestPalindromeRange = (left, right)

#                 left -= 1
#                 right += 1

#         return s[longestPalindromeRange[0]:longestPalindromeRange[1] + 1]

    # refactored expand from single or adjacent characters approach
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        maxPalindromeRange = (0, 0)

        # expand from middle of single or two adjacent characters, to left and right
        for i in range(1, len(s)):
            # find local max palindrome expanding from current single character
            localMaxRange = self.findLongestPalindromeRange(i, i, s)
            maxPalindromeRange = self.getMaxRange(localMaxRange, maxPalindromeRange)

            # find local max palindrome expanding from current and previous character
            localMaxRange = self.findLongestPalindromeRange(i - 1, i, s)
            maxPalindromeRange = self.getMaxRange(localMaxRange, maxPalindromeRange)

        return s[maxPalindromeRange[0]:maxPalindromeRange[1] + 1]

    def getMaxRange(self, range1: tuple[int, int], range2: tuple[int, int]) -> tuple[int, int]:
        if (range1[1] - range1[0]) + 1 > (range2[1] - range2[0]) + 1:
            return range1

        return range2

    def findLongestPalindromeRange(self, left: int, right: int, s: str) -> tuple[int, int]:
        # default local max palindrom range is length of 1 if initial left and right 
        # characters don't match
        localMaxRange = (0, 0)

        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            localMaxRange = (left, right)
            left -= 1
            right += 1

        return localMaxRange
