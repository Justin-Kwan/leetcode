class Solution {
public:
    // optimal hash letter frequency approach
    // time:  O(NM) for N words and M length of longest word
    // space: O(26N + NM) => O(NM) for N words and M length of longest word since at
    //        most N word frequency keys of length 26 in hashmap, and all N words each
    //        with M chars at most stored across hashmap values
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groupedAnagrams;
        vector<vector<string>> groups;

        // insert words into anagram groups keyed by letter frequencies
        for (string &word : strs) {
            int letterFreqs [26] = { 0 };
            for (char &letter : word) {
                ++letterFreqs[int(letter) - int('a')];
            }
            // convert word's letter frequencies into a hashable key (string)
            string freqsHash;
            for (int &freq : letterFreqs) {
                freqsHash += freq + ',';
            }
            groupedAnagrams[freqsHash].push_back(word);
        }

        // collect and return all anagram groups
        for (auto &[_, group] : groupedAnagrams) {
            groups.push_back(group);
        }
        return groups;
    }

    // // suboptimal hash sorted anagram approach
    // // time:  O(N MlogM + N) => O(N(MlogM)) for N words and M length longest word
    // // space: O(2NM) => O(NM) for N words with M max word length worst case, each word
    // //        is only anagram of itself for at most N keys, always N words across all values
    // vector<vector<string>> groupAnagrams(vector<string>& strs) {
    //     unordered_map<string, vector<string>> groupedAnagrams;
    //     vector<vector<string>> groups;

    //     // insert words into anagram groups keyed by sorted word order
    //     for (string &word : strs) {
    //         string sortedWord = word;
    //         sort(sortedWord.begin(), sortedWord.end());
    //         groupedAnagrams[sortedWord].push_back(word);
    //     }

    //     // collect and return all anagram groups
    //     for (auto &[_, group] : groupedAnagrams) {
    //         groups.push_back(group);
    //     }
    //     return groups;
    // }
};
