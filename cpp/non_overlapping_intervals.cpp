class Solution {
public:
    // test cases:
    //           -                 c   n
    // input: [[1,3],[1,2],[2,3],[3,4]]
    // output: 1
    //                 -     -           c   n
    // input: [[1,4],[2,5],[3,6],[4,5],[5,6]]
    // output: 2
    //           -                   c   n
    // input: [[1,10],[2,5],[5,6],[8,10]]
    // output: 1
    //                  -       c    n
    // input: [[1,10],[9,11],[10,20]]
    // output: 1
    //           c     -     -   n
    // input: [[1,2],[1,2],[1,2]]
    // output: 2
    //                 c   n
    // input: [[1,2],[2,3]]
    // output: 0
    //            c  n
    // input: [[0,1]]
    // output: 0
    //
    // optimal greedy two pointers approach
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return 0;
        }
        // sort all intervals by start value to detect adjacent overlaps
        sort(intervals.begin(), intervals.end(), [](auto &interval, auto &other) {
            return interval[0] < other[0];
        });

        int totalErased = 0;
        int cur = 0, next = 1;

        // compare each two intervals and "erase" one when overlap detected
        while (next < intervals.size()) {
            // two adjacent intervals have no overlap, move both pointers up
            if (intervals[cur][1] <= intervals[next][0]) {
                cur = next;
                ++next;
                continue;
            }

            // overlap occurs so one of the two intervals must be removed
            ++totalErased;

            // greedily decide to "erase" the interval with furthest endpoint
            // (local property <=> likely more intersections ahead) since we
            // want to maximize removed overlaps with each "erased" interval

            // if current interval ends further, move it to next to compare next
            // two (skipping past intervals already removed), otherwise if next
            // ends further, move up next and keep same current interval
            if (intervals[cur][1] > intervals[next][1]) {
                cur = next;
            }
            ++next;
        }

        return totalErased;
    }
};
