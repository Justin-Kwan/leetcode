class Solution {
public:
    // optimal min heap approach
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // optimize by returning back nums when top k is n
        if (k == nums.size()) {
            return nums;
        }

        unordered_map<int, int> numsByFreq;
        for (int &num : nums) {
            ++numsByFreq[num];
        }

        // keep track of top k frequent numbers in min heap, always ordered by first entry
        // in pair (frequency in this case)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> topKFreqNums;
        for (auto &[num, freq] : numsByFreq) {
            topKFreqNums.push({ freq, num });
            // eject number of minimum frequency now below top k
            if (topKFreqNums.size() > k) {
                topKFreqNums.pop();
            }
        }

        // dump all top k frequent numbers into return vector
        vector<int> answer;
        while (!topKFreqNums.empty()) {
            answer.push_back(topKFreqNums.top().second);
            topKFreqNums.pop();
        }
        return answer;
    }
};
