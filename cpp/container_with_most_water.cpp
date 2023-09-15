class Solution {
public:
    // test cases:
    //    L
    //    R
    // [1,8,6,2,5,4,8,3,7]
    // maxWaterArea = 49
    // currWaterArea = 8, 49, 18, 40, 16, 15, 4, 6
    //
    //         L
    //            R
    // [1,2,3,18,17,6]
    // maxWaterArea = 17
    //
    //      L
    //         R
    // [1,4,16,32,16,4,1]
    // maxWaterArea = 32
    // currWaterArea = 6, 5, 16, 12, 32, 16
    // (peak, back and forth stalling case)
    //
    // optimal greedy two pointers approach
    int maxArea(vector<int>& heights) {
        int leftPos = 0, rightPos = heights.size() - 1;
        int maxWaterArea = 0;

        // search for two heights yielding max area (two pointers converge to tallest heights
        // since left finds height taller than right, who then tries to height taller than left)
        while (leftPos < rightPos) {
            // current area is bounded by the shortest height
            int curWaterArea = (rightPos - leftPos) * min(heights[leftPos], heights[rightPos]);
            maxWaterArea = max(curWaterArea, maxWaterArea);

            // pointer with the shorter height should shift to find higher one, shifting the
            // shorter pointer *could* result in a rectangle with larger area (or same/smaller)
            //
            // as contradiction, shifting the pointer at taller height cannot increase the
            // area since that next rectangle is always same or smaller because area is limited
            // by the shorter height
            if (heights[leftPos] < heights[rightPos]) {
                ++leftPos;
            }
            else {
                --rightPos;
            }
        }

        return maxWaterArea;
    }
};
