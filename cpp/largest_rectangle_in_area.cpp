class Solution {
public:
    // divide conquer greedy approach
    int largestRectangleArea(vector<int> &heights) {
        return maxPartitionArea(heights, 0, heights.size() - 1);
    }

    int maxPartitionArea(vector<int> &heights, int leftBound, int rightBound) {
        if (leftBound >= rightBound) {
            return 1 * heights[leftBound];
        }

        int middle = (leftBound + rightBound) / 2;
        int leftMaxArea = maxPartitionArea(heights, leftBound, middle);
        int rightMaxArea = maxPartitionArea(heights, middle + 1, rightBound);

        // greedily find max rectangle area crossing over partition line
        int curMaxArea = 0, curMinHeight = INT_MAX;
        int left = middle, right = middle + 1;

        do {
            // current rectangle area bounded by min height seen
            curMinHeight = min({heights[left], heights[right], curMinHeight});
            int curArea = curMinHeight * (right - left + 1);
            curMaxArea = max(curArea, curMaxArea);

            // move other pointer if one has reached the end
            if (left <= leftBound) {
                ++right;
            }
            else if (right >= rightBound) {
                --left;
            }
            // otherwise move left or right to next height that maximizes area
            else if (heights[left - 1] >= heights[right + 1]) {
                --left;
            }
            else {
                ++right;
            }
        }
        while (leftBound <= left && right <= rightBound);

        // max rectangle area in current parition is either max rectangle area
        // in left or right, or max rectangle area crossing middle partition
        return max({ curMaxArea, leftMaxArea, rightMaxArea });
    }
};
