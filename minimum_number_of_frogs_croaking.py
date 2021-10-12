class Solution:
    # optimized greedy
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if croakOfFrogs == "":
            return 0

        charsByCount = { 'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0 }
        
        currentFrogs = 0
        maxConcurrentFrogs = 0

        for char in croakOfFrogs:
            if char not in charsByCount:
                return -1

            if char == 'c':
                currentFrogs += 1
            if char == 'k':
                currentFrogs -= 1

            charsByCount[char] += 1
                
            # ensure all croak instances up to 'k' are in correct order
            # since each char requires at least one correct preceding one
            if charsByCount['c'] < charsByCount['r'] or charsByCount['r'] < charsByCount['o'] or charsByCount['o'] < charsByCount['a'] or charsByCount['a'] < charsByCount['k']:
                return -1

            maxConcurrentFrogs = max(currentFrogs, maxConcurrentFrogs)

        # verify that each croak has same number of chars (each croak is completed)
        if charsByCount['c'] == charsByCount['r'] and charsByCount['r'] == charsByCount['o'] and charsByCount['o'] == charsByCount['a'] and charsByCount['a'] == charsByCount['k']:
            return maxConcurrentFrogs
        
        # a croak that started didn't finish
        return -1
