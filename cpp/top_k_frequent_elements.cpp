class Solution {
private:
    unordered_map<int, int> numFreqs;
    vector<int> uniqueNums;

public:
    // quick select approach
    vector<int> topKFrequent(vector<int> &nums, int kLargest) {
        for (int &num : nums) {
            ++numFreqs[num];
        }

        // create list of numbers without duplicates to avoid including duplicate
        // numbers in top k frequent
        for (auto &[num, _] : numFreqs) {
            uniqueNums.push_back(num);
        }

        int kSmallest = uniqueNums.size() - kLargest;
        quickselect(kSmallest, 0, uniqueNums.size() - 1);

        // collect k final numbers with highest frequencies
        return vector<int>(uniqueNums.begin() + kSmallest, uniqueNums.end());
    }

    void quickselect(int kSmallest, int startPos, int endPos) {
        // kth largest pivot must exist within N numbers, found once start reaches end
        if (startPos == endPos) {
            return;
        }

        // guess that the number at pivot position is kth number in sorted order
        int pivotPos = partition(startPos, endPos);
        if (pivotPos == kSmallest) {
            return;
        }
        // kth sorted order number actually before pivot, update upper bound before repartitioning
        else if (kSmallest < pivotPos) {
            quickselect(kSmallest, startPos, pivotPos - 1);
        }
        // kth sorted order number after before pivot, update lower bound before repartitioning
        else {
            quickselect(kSmallest, pivotPos + 1, endPos);
        }
    }

    // lomuto partition numbers about randomly chose pivot number
    int partition(int startPos, int endPos) {
        int pivotPos = rand() % (endPos - startPos + 1) + startPos;
        int pivotFreq = numFreqs[uniqueNums[pivotPos]];

        // move pivot number out of way to end while we partition around it
        swap(uniqueNums[pivotPos], uniqueNums[endPos]);

        int nextLargerPos = startPos;
        for (int i = startPos; i <= endPos; ++i) {
            // slow pointer swaps with fast pointer and moves together until it stalls
            // at a number larger than pivot, fast pointer then seeks a number smaller
            // than pivot to swap with, slow pointer advances
            if (numFreqs[uniqueNums[i]] < pivotFreq) {
                swap(uniqueNums[nextLargerPos], uniqueNums[i]);
                ++nextLargerPos;
            }
        }
        // paritioning stopped right before pivot number still at end, put it back by
        // swapping with first number of larger right partition
        swap(uniqueNums[nextLargerPos], uniqueNums[endPos]);
        return nextLargerPos;
    }

    // // optimal bucket sort approach
    // vector<int> topKFrequent(vector<int>& nums, int k) {
    //     unordered_map<int, int> numFrequencies;
    //     int maxFrequency = 0;

    //     // construct hashmap of numbers by their frequencies, capture max number frequency
    //     // since in average case, it is less than total numbers requiring less buckets
    //     for (int &num : nums) {
    //         ++numFrequencies[num];
    //         maxFrequency = max(maxFrequency, numFrequencies[num]);
    //     }

    //     // bucket each number by its frequency in fixed array (reverse index by frequency)
    //     vector<vector<int>> frequencyBuckets(maxFrequency);
    //     for (auto &[num, frequency] : numFrequencies) {
    //         frequencyBuckets[frequency - 1].push_back(num);
    //     }

    //     // collect top k frequent numbers from largest to smallest buckets
    //     vector<int> kFrequentNums;
    //     for (int i = frequencyBuckets.size() - 1; i >= 0; --i) {
    //         for (int &num : frequencyBuckets[i]) {
    //             if (kFrequentNums.size() >= k) {
    //                 return kFrequentNums;
    //             }
    //             kFrequentNums.push_back(num);
    //         }
    //     }

    //     return kFrequentNums;
    // }

    // // min heap approach
    // vector<int> topKFrequent(vector<int>& nums, int k) {
    //     // optimize by returning back nums when top k is n
    //     if (k == nums.size()) {
    //         return nums;
    //     }

    //     unordered_map<int, int> numFrequencies;
    //     for (int &num : nums) {
    //         ++numFrequencies[num];
    //     }

    //     // keep track of top k frequent numbers in min heap, always ordered by first entry
    //     // in pair (frequency in this case)
    //     priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> kFrequentNums;
    //     for (auto &[num, frequency] : numFrequencies) {
    //         kFrequentNums.push({ frequency, num });
    //         // eject number of minimum frequency now below top k
    //         if (kFrequentNums.size() > k) {
    //             kFrequentNums.pop();
    //         }
    //     }

    //     // dump all top k frequent numbers into return vector
    //     vector<int> answer;
    //     while (!kFrequentNums.empty()) {
    //         answer.push_back(kFrequentNums.top().second);
    //         kFrequentNums.pop();
    //     }
    //     return answer;
    // }
};
