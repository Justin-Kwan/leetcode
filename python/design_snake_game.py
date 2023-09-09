ROW = 0
COL = 1

# optimal sliding window queue approach
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.curScore = 0
        self.curFoodIndex = 0
        self.foodPath = food
        self.snakePath = collections.deque([(0, 0)])
        self.cachedSnakePath = set([(0, 0)])
        self.nextHeadMoves = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    def move(self, direction: str) -> int:
        curTailPos = self.snakePath[-1]
        nextHeadPos = (
            self.snakePath[0][ROW] + self.nextHeadMoves[direction][ROW],
            self.snakePath[0][COL] + self.nextHeadMoves[direction][COL],
        )

        # check if snake ran into itself but exclude it's last tail since it'll move
        isSnakeSelfBit = nextHeadPos != self.snakePath[-1] and nextHeadPos in self.cachedSnakePath
        isSnakeOutOfBounds = (nextHeadPos[ROW] < 0 or nextHeadPos[ROW] >= self.height or
                              nextHeadPos[COL] < 0 or nextHeadPos[COL] >= self.width)

        if isSnakeOutOfBounds or isSnakeSelfBit:
            return -1

        curFoodPos = None if self.curFoodIndex >= len(self.foodPath) else (
            self.foodPath[self.curFoodIndex][ROW],
            self.foodPath[self.curFoodIndex][COL],
        )
        # grow snake's tail by not removing last block position if ran into food
        if nextHeadPos == curFoodPos:
            self.curScore += 1
            self.curFoodIndex += 1
        # otherwise move snake tail by one block position towards direction
        else:
            self.snakePath.pop()
            self.cachedSnakePath.remove(curTailPos)

        # move snake head by one block position towards direction only after tail is removed to prevent accidentally removing head in circling snake case
        self.snakePath.appendleft(nextHeadPos)
        self.cachedSnakePath.add(nextHeadPos)

        return self.curScore
