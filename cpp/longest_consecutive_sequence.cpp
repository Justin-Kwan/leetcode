class Solution {
public:
    // optimal walk forwards approach
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numbers(nums.begin(), nums.end());
        int maxSeqLength = 0;

        // enumerate consecutive sequences starting from each number in array
        for (int &num : nums) {
            // only begin counting sequence from a starting number, a number begins a sequence
            // if its number below does not exist (every other number in sequence is skipped
            // since it has a previous)
            if (numbers.find(num - 1) == numbers.end()) {
                int curSeqLength = 0;
                for (int curSeqNum = num; numbers.find(curSeqNum) != numbers.end(); ++curSeqNum) {
                    ++curSeqLength;
                }

                maxSeqLength = max(curSeqLength, maxSeqLength);
            }
        }

        return maxSeqLength;
    }

    // // optimal top down dp approach
    // int longestConsecutive(vector<int>& nums) {
    //     unordered_map<int, int> seqLengthAtNum;
    //     for (int num : nums) {
    //         seqLengthAtNum[num] = -1;
    //     }

    //     int maxSeqLength = 0;
    //     for (int num : nums) {
    //         maxSeqLength = max(maxSeqLength, countMaxSequenceAt(num, seqLengthAtNum));
    //     }

    //     return maxSeqLength;
    // }

    // int countMaxSequenceAt(int num, unordered_map<int, int> &seqLengthAtNum) {
    //     // current number not in array so sequence ended
    //     if (seqLengthAtNum.find(num) == seqLengthAtNum.end()) {
    //         return 0;
    //     }
    //     // number is in array and previously computed sequence length upto it
    //     if (seqLengthAtNum[num] > 0) {
    //         return seqLengthAtNum[num];
    //     }

    //     // sequence length ending at current number depends on length ending at
    //     // previous number (+ 1 for itself)
    //     seqLengthAtNum[num] = countMaxSequenceAt(num - 1, seqLengthAtNum) + 1;
    //     return seqLengthAtNum[num];
    // }
};
