class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack = []
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    stack.append((i,j))
        steps = 0
        while stack and freshCount > 0:
            for _ in range(len(stack)):
                x,y = stack.pop(0)
                for delx, dely in [(1,0), (0,1), (-1,0), (0,-1)]:
                    newx, newy = x + delx, y + dely
                    if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] == 1:
                        stack.append((newx, newy))
                        grid[newx][newy] = 2
                        freshCount -= 1
            steps += 1
        if freshCount == 0:
            return steps
        return -1