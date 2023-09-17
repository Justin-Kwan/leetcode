// optimal chunked length approach
class Codec {
public:
    // encode test cases:
    // input:  ["Hello","th ere",",World!"]
    // output: "[5,6,7,]Helloth ere,World!"
    //
    // input:  ["]"]
    // output: "[1,]]"
    //
    // input:  ["", ""]
    // output: "[0,0,]"
    //
    // Encodes a list of strings to a single string.
    string encode(vector<string>& decoded) {
        string encoded;

        // prefix encoded string with lengths of each word, each comma indicates
        // end of word length digits while decoding
        encoded.push_back('[');
        for (string &word : decoded) {
            encoded.append(to_string(word.size()));
            encoded.push_back(',');
        }
        encoded.push_back(']');

        // append characters of all words with no delimiters (since lengths saved)
        for (string &word : decoded) {
            for (char &letter : word) {
                encoded.push_back(letter);
            }
        }

        return encoded;
    }

    // decode test cases:
    //                                    c
    // input:  "[5,6,7,]Helloth ere,World!" wordLengths = [5,6,7]
    // output: ["Hello", "th ere", ",World!"]
    //               c
    // input:  "[1,]]" wordLengths = [1]
    // output: ["]"]
    //                c
    // input:  "[0,0,]" wordLengths = [0,0]
    // output: ["", ""]
    //
    // Decodes a single string to a list of strings.
    vector<string> decode(string encoded) {
        vector<int> wordLengths;
        vector<string> decoded;

        int curPos = 0;
        int wordLength = 0;

        // trim and parms word lengths prefixed to front of encoded string
        while (encoded[curPos] != ']') {
            if (isdigit(encoded[curPos])) {
                wordLength *= 10;
                wordLength += encoded[curPos] - '0';
            }
            if (encoded[curPos] == ',') {
                wordLengths.push_back(wordLength);
                wordLength = 0;
            }
            ++curPos;
        }
        ++curPos;

        // parse and decode each word according to it's length
        for (int &wordLength : wordLengths) {
            string decodedWord;
            for (int _ = 0; _ < wordLength; ++_) {
                decodedWord.push_back(encoded[curPos]);
                ++curPos;
            }
            decoded.push_back(decodedWord);
        }

        return decoded;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
