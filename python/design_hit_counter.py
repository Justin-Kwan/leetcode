# ring buffer approach
class HitCounter:
    TIME_SECONDS = 0
    HIT_COUNT = 1

    def __init__(self):
        self.minutesRetained = 5
        self.head = 0
        self.hitsBySecond = [[0, 0]] * (self.minutesRetained * 60)

    def hit(self, timestamp: int) -> None:
        # hit within current time second window
        if self.hitsBySecond[self.head][self.TIME_SECONDS] == timestamp:
            self.hitsBySecond[self.head][self.HIT_COUNT] += 1
        # hit after latest (not necessarily last) time second window
        else:
            self.head = (self.head + 1) % len(self.hitsBySecond)
            self.hitsBySecond[self.head] = [timestamp, 1]

    def getHits(self, timestamp: int) -> int:
        hitCount = 0

        for hits in self.hitsBySecond:
            # only sum hits in each second window within 5 minutes before timestamp
            if timestamp - hits[self.TIME_SECONDS] < self.minutesRetained * 60:
                hitCount += hits[self.HIT_COUNT]

        return hitCount

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
