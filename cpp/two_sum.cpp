class Solution {
public:
    // optimal single pass hashmap approach
    vector<int> twoSum(vector<int>& nums, int target) {
        // dump all numbers by position into hashmap
        unordered_map<int, int> numsByPos;
        for (int i = 0; i < nums.size(); ++i) {
            // find possible complement previously seen to current number
            // before overwriting previous position with new one if duplicates
            // (target sum pair will be found upon second number looking backwards)
            int complement = target - nums[i];
            if (numsByPos.find(complement) != numsByPos.end() && numsByPos[complement] != i) {
                return {i, numsByPos[complement]};
            }
            numsByPos[nums[i]] = i;
        }

        // no two numbers at different positions sum to target
        return {-1, -1};
    }

    // // hashmap approach
    // vector<int> twoSum(vector<int>& nums, int target) {
    //     // dump all numbers by position into hashmap
    //     unordered_map<int, int> numsByPos;
    //     for (int i = 0; i < nums.size(); ++i) {
    //         numsByPos[nums[i]] = i;
    //     }

    //     for (int i = 0; i < nums.size(); ++i) {
    //         int complement = target - nums[i];
    //         // complement should not be same number at current position
    //         if (numsByPos.find(complement) != numsByPos.end() && numsByPos[complement] != i) {
    //             return {i, numsByPos[complement]};
    //         }
    //     }

    //     // no two numbers at different positions sum to target
    //     return {-1, -1};
    // }
};
