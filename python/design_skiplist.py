class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.below = None

class Skiplist:
    def __init__(self):
        head = Node(float('-inf'))
        head.next = Node(float('inf'))

        self.head = head
        self.levelCount = 1

    def search(self, target: int) -> bool:
        nodePath = self.getNodePath(target)
        potentialTarget = nodePath.pop().next

        return potentialTarget.val == target

    def add(self, num: int) -> None:
        # make space for extra levels at top if exceeds current height
        towerHeight = self.generateTowerHeight()

        for _ in range(self.levelCount - 1, towerHeight):
            newHead = Node(float('-inf'))
            newHead.below = self.head

            newHead.next = Node(float('inf'))
            newHead.next.below = self.head.next

            self.head = newHead
            self.levelCount += 1

        # path of values to last node < num used to relink if added above levels to previous
        nodePath = self.getNodePath(num)
        target = None

        # stack new num onto tower vertically starting from bottom level
        for i in range(0, towerHeight):
            if not nodePath:
                break

            beforeTarget = nodePath.pop()
            afterTarget = beforeTarget.next

            if i == 0:
                target = Node(num)
                target.next = afterTarget
                target.below = None
            else:
                targetBelow = target
                target = Node(num)
                target.next = afterTarget
                target.below = targetBelow

            beforeTarget.next = target

    def generateTowerHeight(self) -> int:
        # add 1 for inserting into bottom level
        towerHeight = 1

        # keep flipping coin, tower height increases while head
        while random.randint(0, 1) != 1:
            towerHeight += 1

        return towerHeight

    def erase(self, num: int) -> bool:
        nodePath = self.getNodePath(num)

        if not nodePath:
            return False

        beforeTarget = nodePath.pop()

        # num not in first level means num must not exist
        if beforeTarget.next.val != num:
            return False

        # start deleting tower vertically
        while beforeTarget.next.val == num:
            # remove target
            beforeTarget.next = beforeTarget.next.next  # no need to relink to new below
            beforeTarget = nodePath.pop()

        # remove empty top sentinel levels (since num was removed from them)
        while self.levelCount >= 2 and self.head.below.next.val == float('inf'):
            self.head.below = self.head.below.below
            self.head.next.below = self.head.next.below.below
            self.levelCount -= 1

        return True

    def getNodePath(self, target: int) -> List[Node]:
        head = self.head
        nodePath = [head]

        # traverse downwards first since top level is always empty
        while head:
            if head.next.val < target:
                head = head.next
            else:
                # add last node < target horizontally to path
                nodePath.append(head)
                head = head.below

        return nodePath

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
