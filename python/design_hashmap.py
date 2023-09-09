# linked list backed bucket approach
class LinkedBucket:
    class Node:
        def __init__(self, key: int = 0, value: int = 0):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self.dummyHead = self.Node()

    def get(self, key: int) -> int:
        head = self.dummyHead.next

        while head:
            if head.key == key:
                return head.value

            head = head.next

        return -1

    def put(self, key: int, value: int):
        prev = self.dummyHead
        head = prev.next

        # update if kv in linked list
        while head:
            if head.key == key:
                head.value = value
                return

            prev = head
            head = head.next

        # attach new kv to end (which is null)
        prev.next = self.Node(key, value)

    def remove(self, key: int):
        prev = self.dummyHead
        head = prev.next

        while head:
            if head.key == key:
                prev.next = head.next
                return

# array backed bucket approach
class ListBucket:
    def __init__(self):
        self.keyValues: List[int] = []

    def getSize(self) -> int:
        return len(self.keyValues)

    def get(self, key: int) -> int:
        # find kv
        for keyValue in self.keyValues:
            if keyValue[0] == key:
                return keyValue[1]

        # kv not found
        return -1

    def put(self, key: int, value: int):
        # update kv if key exists
        for i in range(0, self.getSize()):
            if self.keyValues[i][0] == key:
                self.keyValues[i] = (key, value)
                return

        # add key
        self.keyValues.append((key, value))

    def remove(self, key: int):
        for i in range(0, self.getSize()):
            if self.keyValues[i][0] == key:
                # replace kv with last and truncate
                self.keyValues[i] = self.keyValues[self.getSize() - 1]
                self.keyValues.pop()

                return

class MyHashMap:
    def __init__(self):
        # prime number to reduce "hot buckets", since has
        # only 1 divisor => at most 1 "hot bucket"
        self.bucketCount = 1009
        self.buckets = [None] * self.bucketCount

    def getBucket(self, key: int):
        bucketId = key % self.bucketCount

        # lazily create bucket at hash
        if not self.buckets[bucketId]:
            self.buckets[bucketId] = ListBucket()

        return self.buckets[bucketId]

    def put(self, key: int, value: int) -> None:
        bucket = self.getBucket(key)
        bucket.put(key, value)

    def get(self, key: int) -> int:
        bucket = self.getBucket(key)
        return bucket.get(key)

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)
        bucket.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
