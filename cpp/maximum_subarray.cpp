class Solution {
public:
    // optimal bottom up dp approach
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN, curMaxSum = 0;

        for (int &num : nums) {
            curMaxSum = max(curMaxSum + num, num);
            maxSum = max(curMaxSum, maxSum);
        }
        return maxSum;
    }

    // // suboptimal divide conquer approach
    // int maxSubArray(vector<int>& nums) {
    //     return maxPartitionSum(nums, 0, nums.size() - 1);
    // }

    // int maxPartitionSum(vector<int>& nums, int leftBound, int rightBound) {
    //     if (leftBound >= rightBound) {
    //         return nums[leftBound];
    //     }

    //     int middle = (leftBound + rightBound) / 2;
    //     int leftMaxSum = maxPartitionSum(nums, leftBound, middle);
    //     int rightMaxSum = maxPartitionSum(nums, middle + 1, rightBound);

    //     // find max subaray sum crossing over partition to left and
    //     // max subaray sum crossing over partition to right
    //     int curLeftSum = 0, curLeftMax = nums[middle];
    //     for (int i = middle; i >= leftBound; --i) {
    //         curLeftSum += nums[i];
    //         curLeftMax = max(curLeftSum, curLeftMax);
    //     }
    //     int curRightSum = 0, curRightMax = nums[middle + 1];
    //     for (int i = middle + 1; i <= rightBound; ++i) {
    //         curRightSum += nums[i];
    //         curRightMax = max(curRightSum, curRightMax);
    //     }

    //     // max subarray sum area in current parition is either max sum
    //     // in left or right, or max subarray sum crossing middle partition
    //     return max({ curLeftMax + curRightMax, leftMaxSum, rightMaxSum });
    // }
};
