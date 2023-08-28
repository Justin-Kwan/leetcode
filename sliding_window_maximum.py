class Solution:
    # lazy heap approach
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # track k largest numbers in each window, lazily delete stale max
        # values from previous windows instead of scanning heap to delete
        # last of each window
        kWindowNums, maxWindows = [], []

        for i in range(len(nums)):
            heapq.heappush(kWindowNums, (-nums[i], i))
            # cannot find max until first window built
            if i < k - 1:
                continue

            # delete stale max values outside current window, from previous
            while (numPos := kWindowNums[0][1]) < i - k + 1:
                heapq.heappop(kWindowNums)

            # collect max number actually within current window
            maxWindowNum, _ = kWindowNums[0]
            maxWindows.append(-maxWindowNum)

        return maxWindows
