class Solution {
public:
    // optimal greedy approach
    int jump(vector<int>& nums) {
        // starting at first number, try to reach end with minimum jumps needed
        int minSteps = 0, curPos = 0;

        while (curPos < nums.size() - 1) {
            ++minSteps;

            // exit when current jump can reach or surpass end of list
            if (curPos + nums[curPos] >= nums.size() - 1) {
                curPos += nums[curPos];
                break;
            }

            // greedily look for best next position within current jump range
            int bestNextPos = curPos + 1;
            for (int nextPos = curPos + 1; nextPos < curPos + 1 + nums[curPos]; ++nextPos) {
                // take next position within range that can "jump" to furthest position 
                if (nextPos + nums[nextPos] > bestNextPos + nums[bestNextPos]) {
                    bestNextPos = nextPos;
                }
            }

            // "jump" to the next position
            curPos = bestNextPos;
        }

        return minSteps;
    }
};
