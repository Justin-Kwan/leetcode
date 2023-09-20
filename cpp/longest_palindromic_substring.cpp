class Solution {
public:
    // optimal expand from center approach
    string longestPalindrome(string s) {
        if (s.empty()) {
            return "";
        }

        pair<int, int> maxPalindromeRange;

        for (int i = 0; i < s.size(); ++i) {
            // expand from single character to find odd length palindrome
            maxPalindromeRange = maxRange(maxPalindromeRange, findPalindrome(s, i, i));
            // expand from two adjacent characters to find even length palindrome
            maxPalindromeRange = maxRange(maxPalindromeRange, findPalindrome(s, i, i + 1));
        }

        int maxPalidromeLength = maxPalindromeRange.second - maxPalindromeRange.first + 1;
        return s.substr(maxPalindromeRange.first, maxPalidromeLength);
    }

    pair<int, int> findPalindrome(string &s, int leftPos, int rightPos) {
        // keep expanding while both pointers in range and letters match
        while (0 <= leftPos && rightPos < s.size() && s[leftPos] == s[rightPos]) {
            --leftPos;
            ++rightPos;
        }
        // if two adjacent letters do not match, positions will be crossed which
        // will compute to length of 0 when added by 1
        return { leftPos + 1, rightPos - 1 };
    }

    pair<int, int> maxRange(pair<int, int> range, pair<int, int> other) {
        if ((range.second - range.first + 1) > (other.second - other.first + 1)) {
            return range;
        }
        return other;
    }
};
