class Solution {
public:
    // optimal letter frequency approach
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        int letterFreqs[26] = { 0 };
        for (char &letter : s) {
            ++letterFreqs[int(letter) - int('a')];
        }

        for (char &letter : t) {
            --letterFreqs[int(letter) - int('a')];
            // word t had more of current letter than word s
            if (letterFreqs[int(letter) - int('a')] < 0) {
                return false;
            }
        }

        // length of t and s is same up to here, do not need to check if
        // t had less letters than s
        return true;    
    }
};
