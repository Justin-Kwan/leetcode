class Solution {
public:
    // stack approach
    bool isValid(string s) {
        stack<char> openBrackets;
        unordered_map<char, char> bracketPairs = { {'(', ')'}, {'[', ']'}, {'{', '}'} };

        for (char &bracket : s) {
            // open bracket
            if (bracketPairs.find(bracket) != bracketPairs.end()) {
                openBrackets.push(bracket);
                continue;
            }
            // last open bracket should exist and match current closed bracket
            if (openBrackets.empty() || bracket != bracketPairs[openBrackets.top()]) {
                return false;
            }
            openBrackets.pop();
        }
        // check if not enough closed brackets for open brackets
        return openBrackets.empty();
    }
};
