class Solution {
public:
    // optimal bottom up dp approach
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> productsExceptSelf(nums.size(), 1);

        // compute and store product to right of each number
        for (int i = nums.size() - 2; i >= 0; --i) {
            productsExceptSelf[i] = productsExceptSelf[i + 1] * nums[i + 1];
        }

        // compute and roll over left products of each number and multiply by 
        // right products for total product to left and right of each number
        int leftProduct = 1;
        for (int i = 0; i < nums.size(); ++i) {
            productsExceptSelf[i] = leftProduct * productsExceptSelf[i];
            leftProduct *= nums[i];
        }

        return productsExceptSelf;
    }
};
