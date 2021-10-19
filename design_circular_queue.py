from threading import Lock

class MyCircularQueue:
    def __init__(self, k: int):
        self.values = [-1] * k
        self.length = k

        self.frontIndex = 0
        self.nextIndex = 0

        self.readWriteLock = Lock()

    def enQueue(self, value: int) -> bool:
        # should be atomic
        try:
            self.readWriteLock.acquire()

            if self.isFull():      # prevent race here
                return False

            self.values[self.nextIndex % self.length] = value
            self.nextIndex += 1    # point to next empty slot
        finally:
            self.readWriteLock.release()

        return True

    def deQueue(self) -> bool:
        # should be atomic
        try:
            self.readWriteLock.acquire()

            if self.isEmpty():     # prevent race here resulting in front = 1 + rear
                return False

            self.values[self.frontIndex % self.length] = -1
            self.frontIndex += 1
        finally:
            self.readWriteLock.release()

        return True

    def Front(self) -> int:
        return self.values[self.frontIndex % self.length]

    def Rear(self) -> int:
        return self.values[(self.nextIndex - 1) % self.length]

    def isEmpty(self) -> bool:
        # if front pointer has dequeued all the way to next slot pointer
        return self.frontIndex == self.nextIndex

    def isFull(self) -> bool:
        # if next empty slot is first slot (filled all the way around)
        return self.nextIndex - self.frontIndex == self.length

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
