class Solution {
public:
    // test cases:
    // input: [[0,30],[5,10],[15,20]] roomExpiries = [20, 30]
    // output: 2
    //
    // input: [[2,4],[7,10]] roomExpiries = [10]
    // output: 1
    //
    // input: [[1,4],[2,5],[3,6],[4,5]] roomExpiries = [4,5,6]
    // output: 3
    //
    // input: [[5,6]] roomExpiries: [6]
    // output: 1
    //
    // input: []
    // output: 0
    //
    // optimal sorting heap approach
    int minMeetingRooms(vector<vector<int>>& intervals) {
        // sort all meeting intervals by start times
        sort(intervals.begin(), intervals.end(), [](auto &interval, auto &other) {
            return interval[0] < other[0];
        });

        priority_queue<int, vector<int>, greater<int>> roomExpiries;

        for (auto &meeting : intervals) {
            int meetingStart = meeting[0], meetingEnd = meeting[1];
            // can reuse earliest expiring room, pop it (update room's expiry below)
            if (!roomExpiries.empty() && roomExpiries.top() <= meetingStart) {
                roomExpiries.pop();
            }
            // either updating the new expiry of a reused room (already expired)
            // or checking out a new room if non exist or all rooms currently in
            // use with future expiries
            roomExpiries.push(meetingEnd);
        }

        return roomExpiries.size();
    }
};
