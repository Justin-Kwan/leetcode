class Solution:
    # brute force
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # cache to memoize if substring after certain index can be made using words in dict
        cache: Dict[int, bool] = {}
        return self.isComprisedOfDict(s, 0, 0, set(wordDict), cache)

    def isComprisedOfDict(self, s: str, leftPtr: int, rightPtr: int, wordDict: set[str], cache: Dict[int, bool]):
        # when prev substring chunk in dict, so now pointer has "fallen off" string
        if rightPtr == len(s):
            return True
        
        for i in range(leftPtr, len(s)):
            
            # if current substring in dict
            if s[leftPtr : i + 1] in wordDict:
                isRemainingStringComprisedOfDict = ((i + 1) in cache and cache[i + 1])
                isRemainingStringNotComprisedOfDict = (i + 1) in cache and cache[i + 1] == False

                if isRemainingStringNotComprisedOfDict:
                    continue

                # if rest of string can be made from words in dict
                if isRemainingStringComprisedOfDict or self.isComprisedOfDict(s, i + 1, i + 1, wordDict, cache):
                    # from current char, remaining substring is comprisable from dict
                    cache[leftPtr] = True
                    return True

        # all substrings in rest of all string cannot be made from words in dict
        cache[leftPtr] = False
        return False

