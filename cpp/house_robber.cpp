class Solution {
public:
    // optimal bottom up dp approach
    int rob(vector<int> &nums) {
        int maxRobbedAt;
        int maxRobbedPrevPrev = 0, maxRobbedPrev = 0;

        for (int i = 0; i < nums.size(); ++i) {
            // max robbable sum from current house is either max robbable from previous
            // (without current), or current house + max robbable from 2 houses before
            maxRobbedAt = max(maxRobbedPrev, nums[i] + maxRobbedPrevPrev);
            maxRobbedPrevPrev = maxRobbedPrev;
            maxRobbedPrev = maxRobbedAt;
        }
        return maxRobbedAt;
    }

    // // top down dp approach
    // int rob(vector<int> &nums) {
    //     if (nums.empty()) {
    //         return 0;
    //     }

    //     unordered_map<int, int> cache;
    //     return maxRobbedFrom(nums, cache, 0);
    // }

    // int maxRobbedFrom(vector<int> &nums, unordered_map<int, int> &cache, int housePos) {
    //     // reached an invalid neigbor house out of range
    //     if (housePos >= nums.size()) {
    //         return 0;
    //     }
    //     // hit cache for max robbable sum already computed from current house
    //     if (cache.find(housePos) != cache.end()) {
    //         return cache[housePos];
    //     }

    //     // max robbable sum from current house is either max robbable from next
    //     // (without current), or current house + max robbable from 2 houses down
    //     int maxRobbedAt = max(
    //         maxRobbedFrom(nums, cache, housePos + 1),
    //         nums[housePos] + maxRobbedFrom(nums, cache, housePos + 2));

    //     cache[housePos] = maxRobbedAt;
    //     return maxRobbedAt;
    // }
};
