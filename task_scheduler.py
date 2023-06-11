EXPIRY = 1

class Solution:
    # greedy queue approach
    def leastInterval(self, tasks: List[str], cooldown: int) -> int:
        # create map of task frequencies to greedily schedule most frequent first
        taskCounts = Counter(tasks)
        topTaskCounts = list(taskCounts.values())
        heapq._heapify_max(topTaskCounts)

        curCycle = 0
        coolingTasks = collections.deque()

        # execute all tasks in run queue (heap)
        while topTaskCounts or coolingTasks:
            curCycle += 1

            if topTaskCounts:
                taskCount = heapq._heappop_max(topTaskCounts)
                # only keep and cooldown threads who have more tasks to run
                if taskCount > 1:
                    coolingTasks.append((taskCount - 1, curCycle + cooldown))
            # check if any task is done cooling at end of clock cycle
            if coolingTasks and coolingTasks[0][EXPIRY] == curCycle:
                taskCount, _ = coolingTasks.popleft()
                # _heappush_max()
                topTaskCounts.append(taskCount)
                heapq._siftdown_max(topTaskCounts, 0, len(topTaskCounts) - 1)

        return curCycle
