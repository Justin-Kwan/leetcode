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

    // // optimal monotonic stack approach
    // int largestRectangleArea(vector<int> &heights) {
    //     // stack stores monotonically increasing heights, defer computing area of
    //     // rectangle from it once a shorter height no longer accomondates
    //     stack<pair<int, int>> seenHeights;
    //     int maxArea = 0;

    //     for (int i = 0; i < heights.size(); ++i) {
    //         // assume rectangle at current bar height starts from current position
    //         int startPos = i;

    //         // reached smaller bar height, compute areas for previous taller rectangles
    //         // since we know they end here
    //         while (!seenHeights.empty() && seenHeights.top().first > heights[i]) {
    //             auto &[prevHeight, prevPos] = seenHeights.top(); seenHeights.pop();
    //             maxArea = max(prevHeight * (i - prevPos), maxArea);
    //             // rectangle at shorter current height could start from previous
    //             // taller height's position so carry it over
    //             startPos = prevPos;
    //         }

    //         seenHeights.push(make_pair(heights[i], startPos));
    //     }

    //     // pop out and compute rectangle areas from any remaining increasing heights
    //     while (!seenHeights.empty()) {
    //         auto &[prevHeight, prevPos] = seenHeights.top(); seenHeights.pop();
    //         int areaFromHeight = prevHeight * (heights.size() - prevPos);
    //         maxArea = max(areaFromHeight, maxArea);
    //     }

    //     return maxArea;
    // }
};
