class Solution {
public:
    // test cases:
    //                                      i
    // input:  [[1,2],[3,5],[6,7],[8,10],[12,16]] newInterval = [4,8],[3,10]
    // output: [[1,2],[3,10],[12,16]]
    //                            i
    // input:  [[2,3],[4,5],[6,7]] newInterval = [1,8]
    // output: [[1,8]]
    //                      i
    // input:  [[1,1],[2,2]] newInterval = [2,2]
    // output: [[1,1],[2,2]]
    //                i
    // input:  [[1,1]] newInterval = [2,2]
    // output: [[1,1],[2,2]]
    //                i
    // input:  [[1,1]] newInterval = [0,2]
    // output: [[0,2]]
    //            i
    // input:  [[1,1]] newInterval = [0,0]
    // output: [[0,0][1,1]]
    //          i
    // input:  [] newInterval = [0,0]
    // output: [[0,0]]
    //
    // optimal greedy approach
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval) {
        vector<vector<int>> mergedIntervals;

        for (int i = 0; i < intervals.size(); ++i) {
            // new interval falls before current one, add it and remaining intervals
            if (newInterval[1] < intervals[i][0]) {
                mergedIntervals.push_back(newInterval);
                vector<vector<int>> rest = { intervals.begin() + i, intervals.end() };
                mergedIntervals.insert(mergedIntervals.end(), rest.begin(), rest.end());
                return mergedIntervals;
            }
            // new interval is beyond current one, add current one and continue
            else if (intervals[i][1] < newInterval[0]) {
                mergedIntervals.push_back(intervals[i]);
            }
            // new interval overlaps with current interval, expand new interval
            // by taking max of overlapping start and end bounds (could absorb)
            else {
                newInterval[0] = min(intervals[i][0], newInterval[0]);
                newInterval[1] = max(intervals[i][1], newInterval[1]);
            }
        }

        // new interval is either beyond all other intervals, or it expanded and
        // absorbed all other intervals all the way to the end
        mergedIntervals.push_back(newInterval);
        return mergedIntervals;
    }
};
