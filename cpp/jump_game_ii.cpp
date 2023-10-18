class Solution {
public:
    // optimal simplified greedy approach
    int jump(vector<int> &nums) {
        if (nums.empty() || nums.size() == 1) {
            return 0;
        }

        int stops = 1;
        int rangeEnd = nums[0];
        int bestNextPos = INT_MIN, furthestJump = INT_MIN;

        // greedily choose next position within range that can jump furthest distance
        for (int curPos = 1; curPos < nums.size() - 1; ++curPos) {
            if (curPos + nums[curPos] > furthestJump) {
                bestNextPos = curPos;
                furthestJump = curPos + nums[curPos];
            }

            // once reached current range end, update next jump range's end position
            if (curPos == rangeEnd) {
                ++stops;
                rangeEnd = furthestJump;
            }
        }

        return stops;
    }

    // // optimal greedy approach
    // int jump(vector<int>& nums) {
    //     // starting at first number, try to reach end with minimum jumps needed
    //     int minSteps = 0, curPos = 0;
    //     int rangeEnd = 0;

    //     while (curPos < nums.size() - 1) {
    //         ++minSteps;

    //         // exit when current jump can reach or surpass end of list
    //         if (curPos + nums[curPos] >= nums.size() - 1) {
    //             curPos += nums[curPos];
    //             break;
    //         }

    //         // greedily look for best next position within current jump range
    //         int bestNextPos = rangeEnd + 1;
    //         for (int nextPos = rangeEnd + 1; nextPos <= curPos + nums[curPos]; ++nextPos) {
    //             // take next position within range that can "jump" to furthest position 
    //             if (nextPos + nums[nextPos] > bestNextPos + nums[bestNextPos]) {
    //                 bestNextPos = nextPos;
    //             }
    //         }
    //         rangeEnd = curPos + nums[curPos];

    //         // "jump" to the next position
    //         curPos = bestNextPos;
    //     }

    //     return minSteps;
    // }
};
