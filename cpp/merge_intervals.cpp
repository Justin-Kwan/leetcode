class Solution {
public:
    // test cases:
    //                        i
    // input: [[1,3],[2,6],[8,10],[15,18]] lastMerged = [1,3], [1,6] - [8,10]
    // output: [[1,6],[8,10],[15,18]]
    //                  i
    // input:  [[1,4],[4,5]] lastMerged = [1,4], [1,5]
    // output: [[1,5]]
    //                        i
    // input:  [[1,1],[2,2],[3,4]] lastMerged = [1,1] - [2,2] - [3,4]
    // output: [[1,1],[2,2],[3,4]]
    //                                     i
    // input:  [[1,10],[1,2],[1,3],[2,6],[4,11]] lastMerged = [1,11]
    // output: [[1,11]]
    //            i
    // input:  [[3,5]] lastMerged = [3,5]
    // output: [[3,5]]
    //                  i
    // input:  [[2,2],[2,3]] lastMerged = [2,2], [2,3]
    // output: [[2,3]]
    //                 i
    // input:  [[2,3][2,2]] lastMerged = [2,3]
    // output: [[2,3]]
    // 
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return {};
        }

        // sort all intervals by starting key
        sort(intervals.begin(), intervals.end(), [](auto &interval, auto &other) {
            return interval[0] < other[0];
        });

        // compare all future intervals against last merged interval either expand it
        // or insert current interval
        vector<vector<int>> mergedIntervals = { intervals[0] };

        for (auto &interval : intervals) {
            auto &lastMerged = mergedIntervals.back();

            if (lastMerged[1] < interval[0]) {
                // current interval comes after last merged interval so append it
                // and compare future intervals against it (and expand/absorb)
                mergedIntervals.push_back(interval);
            }
            else {
                // last merged interval's end crosses current interval's start so
                // take max of both ends
                //
                // last merged interval should keep its start since it is always
                // less or equal than current interval's start (by sorting)
                lastMerged[1] = max(lastMerged[1], interval[1]);
            }
        }

        return mergedIntervals;
    }
};
