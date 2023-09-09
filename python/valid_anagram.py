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
            else:
                charsByCount[char] -= 1

        # verify that all characters have a count of 0 in map
        for char in charsByCount:
            if charsByCount[char] < 0:
                return False

        return True
