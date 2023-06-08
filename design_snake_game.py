# sliding window queue approach
class SnakePosition:
    def __init__(self, row: int, col: int, direction: str):
        self.row = row
        self.col = col
        self.direction = direction

    def nextHead(self, newDirection: str):
        match newDirection:
            case "R":
                return SnakePosition(self.row, self.col + 1, newDirection)
            case "L":
                return SnakePosition(self.row, self.col - 1, newDirection)
            case "U":
                return SnakePosition(self.row - 1, self.col, newDirection)
            case "D":
                return SnakePosition(self.row + 1, self.col, newDirection)
            case other:
                return self

    def nextTail(self):
        # extend tail to move in same direction as current tail block
        match self.direction:
            case "R":
                return SnakePosition(self.row, self.col - 1, self.direction)
            case "L":
                return SnakePosition(self.row, self.col + 1, self.direction)
            case "U":
                return SnakePosition(self.row + 1, self.col, self.direction)
            case "D":
                return SnakePosition(self.row - 1, self.col, self.direction)
            case other:
                return self

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.currentScore = 0

        # reverse list of foods to access and pop each food at a time
        self.foodPositions = []
        for i in range(len(food) - 1, -1, -1):
            self.foodPositions.append((food[i][0], food[i][1]))

        self.snakePositions = collections.deque()
        self.cachedSnakePositions = set()

    def move(self, direction: str) -> int:
        # lazily set first snake position block in queue to capture initial direction
        if len(self.cachedSnakePositions) == 0:
            self.snakePositions.append(SnakePosition(0, 0, direction))
            self.cachedSnakePositions.add((0, 0))

        nextHead = self.snakePositions[0].nextHead(direction)

        # remove last tail block to make space for moved head if snake is circing
        oldTailPosition = self.snakePositions.pop()
        self.cachedSnakePositions.remove((oldTailPosition.row, oldTailPosition.col))

        # check if snake has reached out of bounds or ran into itself
        if (not self.isPositionWithinBounds(nextHead) or
            (nextHead.row, nextHead.col) in self.cachedSnakePositions):
            return -1

        # move snake by one block position in direction
        self.snakePositions.appendleft(nextHead)
        self.cachedSnakePositions.add((nextHead.row, nextHead.col))

        # check if snake moved into a block with food
        if self.foodPositions and (nextHead.row, nextHead.col) == self.foodPositions[-1]:
            # extend snake at tail following same tail movement direction
            nextTail = self.snakePositions[-1].nextTail()
            self.snakePositions.append(nextTail)
            self.cachedSnakePositions.add((nextTail.row, nextTail.col))
            self.foodPositions.pop()
            self.currentScore += 1

        return self.currentScore

    def isPositionWithinBounds(self, position: SnakePosition) -> bool:
        return (0 <= position.row and position.row < self.height and
                0 <= position.col and position.col < self.width)

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
