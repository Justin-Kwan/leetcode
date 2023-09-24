class Solution {
public:
    // optimal monotonic stack approach
    int maximalRectangle(vector<vector<char>> &matrix) {
        if (matrix.empty()) {
            return 0;
        }

        int maxArea = 0;
        vector<int> heightsAtRow(matrix[0].size(), 0);

        // compute height at each cell row by row, then compute max
        // histogram rectangle from each row
        for (int row = 0; row < matrix.size(); ++row) {
            for (int col = 0; col < matrix[row].size(); ++col) {
                if (matrix[row][col] == '0') {
                    heightsAtRow[col] = 0;
                }
                else {
                    ++heightsAtRow[col];
                }
            }
            maxArea = max(maxArea, largestRectangleArea(heightsAtRow));
        }

        return maxArea;
    }

    int largestRectangleArea(vector<int> &heights) {
        // stack stores monotonically increasing heights, defer computing area of
        // rectangle from it once a shorter height no longer accomondates
        stack<pair<int, int>> seenHeights;
        int maxArea = 0;

        for (int i = 0; i < heights.size(); ++i) {
            // assume rectangle at current bar height starts from current position
            int startPos = i;

            // reached smaller bar height, compute areas for previous taller rectangles
            // since we know they end here
            while (!seenHeights.empty() && seenHeights.top().first > heights[i]) {
                auto &[prevHeight, prevPos] = seenHeights.top(); seenHeights.pop();
                maxArea = max(prevHeight * (i - prevPos), maxArea);
                // rectangle at shorter current height could start from previous
                // taller height's position so carry it over
                startPos = prevPos;
            }

            seenHeights.push(make_pair(heights[i], startPos));
        }

        // pop out and compute rectangle areas from any remaining increasing heights
        while (!seenHeights.empty()) {
            auto &[prevHeight, prevPos] = seenHeights.top(); seenHeights.pop();
            int areaFromHeight = prevHeight * (heights.size() - prevPos);
            maxArea = max(areaFromHeight, maxArea);
        }

        return maxArea;
    }
};
