class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsByCount = {}

        if len(s) != len(t):
            return False

        # dump s's characters in map with count
        for char in s:
            if char not in charsByCount:
                charsByCount[char] = 1
            else:
                charsByCount[char] += 1

        # decrement count by all characters in t
        for char in t:
            if char not in charsByCount:
                return False

            charsByCount[char] -= 1
            if charsByCount[char] < 0:
                return False

        # length of t and s is same up to here, do not need to check if
        # t had less letters than s (any letter frequencies >= 1)
        return True
