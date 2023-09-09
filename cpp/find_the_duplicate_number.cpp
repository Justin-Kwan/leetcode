class Solution {
public:
    // optimal floyd's algorithm approach
    int findDuplicate(vector<int> &nums) {
        if (nums.empty()) {
            return -1;
        }

        int slow = 0, fast = 0;
        // first find node where fast pointer reaches slow in cycle
        // (which always exists)
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // find duplicate number at first "node" of cycle, which is always
        // same distance from collision "node" as from list head (slow finds
        // first cycle "node" from head again)
        slow = 0;
        while (slow != fast) {
            fast = nums[fast];
            slow = nums[slow];
        }

        // duplicate number is always first "node" of cycle since it points
        // to other indexes of numbers which will eventually point back
        return slow;
    }

    // // optimal modify array approach
    // int findDuplicate(vector<int> &nums) {
    //     for (int &num : nums) {
    //         // take positive number since it may have been marked for 
    //         // another number
    //         int curNum = abs(num);

    //         // current number already seen and is duplicate if value at
    //         // same index as current number already flipped to negative
    //         // (only works since all given numbers are positive)
    //         if (nums[curNum - 1] < 0) {
    //             return curNum;
    //         }
    //         // otherwise current number not seen, so mark it as seen
    //         nums[curNum - 1] *= -1;
    //     }
    //     return -1;
    // }

    // // set approach
    // int findDuplicate(vector<int> &nums) {
    //     unordered_set<int> numsLookup;
    //     for (int &num : nums) {
    //         // duplicate number already in set if iterator not at end
    //         if (numsLookup.find(num) != numsLookup.end()) {
    //             return num;
    //         }
    //         numsLookup.insert(num);
    //     }
    //     return -1;
    // }
};
