class Solution:
    # optimal monotonic queue approach
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # track k largest numbers in each window, stale max value is
        # immediately deleted at the next window where out of range
        kMaxNums, maxWindows = collections.deque([]), []

        for i in range(len(nums)):
            # delete smaller values to left of new value in window,
            # they can never be max of current/future windows
            while kMaxNums and (minNum := kMaxNums[-1][0]) < nums[i]:
                kMaxNums.pop()
            kMaxNums.append((nums[i], i))

            # each max window value is immediately removed once stale
            # and outside of future window
            if (maxNumPos := kMaxNums[0][1]) < i - k + 1:
                kMaxNums.popleft()

            # only collect max window value after first window built
            if i >= k - 1:
                maxWindowNum, _ = kMaxNums[0]
                maxWindows.append(maxWindowNum)

        return maxWindows

    # # lazy heap approach
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     # track k largest numbers in each window, lazily delete stale max
    #     # values from previous windows instead of scanning heap to delete
    #     # last of each window
    #     kMaxNums, maxWindows = [], []

    #     for i in range(len(nums)):
    #         heapq.heappush(kMaxNums, (-nums[i], i))
    #         # cannot find max until first window built
    #         if i < k - 1:
    #             continue

    #         # delete stale max values outside current window, from previous
    #         while (maxNumPos := kMaxNums[0][1]) < i - k + 1:
    #             heapq.heappop(kMaxNums)

    #         # collect max number actually within current window
    #         maxWindowNum, _ = kMaxNums[0]
    #         maxWindows.append(-maxWindowNum)

    #     return maxWindows
