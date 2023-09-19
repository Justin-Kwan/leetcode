class Solution {
public:
    // optimal sorting approach
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto &interval, auto &other) {
            return interval[0] < other[0];
        });

        for (int i = 1; i < intervals.size(); ++i) {
            // found a meeting that ends after the next one starts (overlap)
            if (intervals[i - 1][1] > intervals[i][0]) {
                return false;
            }
        }

        return true;
    }
};
