class Solution {
public:
    // optimal bottom up dp approach
    int longestCommonSubsequence(string text1, string text2) {
        // subproblem is length of longest common subsequence up to every ith and jth position
        // DP[i][j] = {
        //     1,                             if i = 0 and j = 0 and S[0] = S2[0]
        //     0,                             if i = 0 and j = 0 and S[0] != S2[0]
        //     DP[i-1][j-1] + 1,              if i > 0 and j > 0 and S1[i] = S2[j]
        //     max{ DP[i-1][j], DP[i][j-1] }, if i > 0 and j > 0 and S1[i] != S2[j]
        // }

        vector<vector<int>> lcsAtPair(text1.size() + 1, vector<int>(text2.size() + 1, 0));

        for (int i = text1.size() - 1; i >= 0; --i) {
            for (int j = text2.size() - 1; j >= 0; --j) {
                if (text1[i] == text2[j]) {
                    lcsAtPair[i][j] = lcsAtPair[i + 1][j + 1] + 1;
                }
                else {
                    lcsAtPair[i][j] = max(lcsAtPair[i + 1][j], lcsAtPair[i][j + 1]);
                }
            }
        }

        return lcsAtPair[0][0];
    }

    // // optimal top down dp approach
    // int longestCommonSubsequence(string text, string other) {
    //     // cache subproblems of lcs length from each link between both strings
    //     // (2D matrix for cartesian product of all character positions)
    //     vector<vector<int>> cache(text.size(), vector<int>(other.size(), -1));
    //     return lcsFrom(text, other, cache, 0, 0);
    // }

    // int lcsFrom(string &text, string &other, vector<vector<int>> &cache, int textPos, int otherPos) {
    //     // no more common subsequences if one of the strings is exhaused
    //     if (textPos >= text.size() || otherPos >= other.size()) {
    //         return 0;
    //     }
    //     // previously computed lcs length from current link between both strings
    //     if (cache[textPos][otherPos] >= 0) {
    //         return cache[textPos][otherPos];
    //     }

    //     int maxLength = 0;
    //     // max sequence length from both string positions depends on max length after
    //     // current link (current text character matches other)
    //     if (text[textPos] == other[otherPos]) {
    //         maxLength = 1 + lcsFrom(text, other, cache, textPos + 1, otherPos + 1);
    //     }
    //     // otherwise try finding max length from every possible link pairing permutation
    //     // between future letters in both strings which will find all possible matches
    //     // (instead of forward scanning other for next matching letter)
    //     else {
    //         maxLength = max(lcsFrom(text, other, cache, textPos + 1, otherPos),
    //                         lcsFrom(text, other, cache, textPos, otherPos + 1));
    //     }

    //     cache[textPos][otherPos] = maxLength;
    //     return maxLength;
    // }

    // // top down dp approach
    // int longestCommonSubsequence(string text, string other) {
    //     // cache subproblems of lcs length from each link between both strings
    //     // (2D matrix for cartesian product of all character positions)
    //     vector<vector<int>> cache(text.size(), vector<int>(other.size(), -1));
    //     return lcsFrom(text, other, cache, 0, 0);
    // }

    // int lcsFrom(string &text, string &other, vector<vector<int>> &cache, int textPos, int otherPos) {
    //     // no more common subsequences if one of the strings is exhaused
    //     if (textPos >= text.size() || otherPos >= other.size()) {
    //         return 0;
    //     }
    //     // previously computed lcs length from current link between both strings
    //     if (cache[textPos][otherPos] >= 0) {
    //         return cache[textPos][otherPos];
    //     }

    //     // try establish link from current letter in text to matching letter in other
    //     int maxLengthWithLink = 0, nextOtherPos = other.find(text[textPos], otherPos);
    //     if (nextOtherPos != string::npos) {
    //         maxLengthWithLink = 1 + lcsFrom(text, other, cache, textPos + 1, nextOtherPos + 1);
    //     }
    //     // try finding max length when establishing no link from current text letter
    //     int maxLengthWithoutLink = lcsFrom(text, other, cache, textPos + 1, otherPos);

    //     // max sequence length from both string positions depends on max length after
    //     // current link found (current text character matches other) or max length if
    //     // no link established (when no matching letter in other or current link blocks
    //     // more optimal lengths)
    //     cache[textPos][otherPos] = max(maxLengthWithLink, maxLengthWithoutLink);
    //     return cache[textPos][otherPos];
    // }
};
