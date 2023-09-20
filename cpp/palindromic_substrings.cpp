class Solution {
public:
    // suboptimal top down dp approach
    int countSubstrings(string s) {
        int totalPalindromes = 0;
        unordered_map<string, bool> cache;

        // check whether every possible substring range is a palindrome
        for (int i = 0; i < s.size(); ++i) {
            for (int j = i; j < s.size(); ++j) {
                if (isPalindromeRange(s, i, j, cache)) {
                    ++totalPalindromes;
                }
            }
        }

        return totalPalindromes;
    }

    bool isPalindromeRange(string &s, int leftPos, int rightPos, unordered_map<string, bool> &cache) {
        // single letter is trivially a palindrome, return true when bounds crossed
        // so previous call from two adjacent letters can be evaluated for palindrome
        if (rightPos <= leftPos) {
            return true;
        }

        // palindromity of current range already computed when larger symmetric outer
        // range checked
        //
        // hack to store multikey entries (ex. tuple or pair) within unordered_map
        string cacheKey = to_string(leftPos) + "," + to_string(rightPos);
        if (cache.find(cacheKey) != cache.end()) {
            return cache[cacheKey];
        }

        // current substring range is a palindrome only if inner substring range within
        // (left + 1) to (right - 1) is a palindrome too, subproblem
        //
        // cache whether inner ranges are palindromes to avoid recomputing and checking
        // smaller inner ranges once two iterating indices reach in the future (triangle)
        cache[cacheKey] = s[leftPos] == s[rightPos] && isPalindromeRange(s, leftPos + 1, rightPos - 1, cache);
        return cache[cacheKey];
    }

    // // optimal expand from center approach
    // int countSubstrings(string s) {
    //     int totalPalindromes = 0;
    //     for (int i = 0; i < s.size(); ++i) {
    //         totalPalindromes += countPalindromesFrom(s, i, i);
    //         totalPalindromes += countPalindromesFrom(s, i, i + 1);
    //     }
    //     return totalPalindromes;
    // }

    // int countPalindromesFrom(string &s, int leftPos, int rightPos) {
    //     int totalPalindromes = 0;
    //     // each extra layer of letters at front and end added is another unique palindrome
    //     while (0 <= leftPos && rightPos < s.size() && s[leftPos] == s[rightPos]) {
    //         ++totalPalindromes;
    //         --leftPos;
    //         ++rightPos;
    //     }
    //     return totalPalindromes;
    // }
};
