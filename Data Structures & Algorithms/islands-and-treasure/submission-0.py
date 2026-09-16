class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi source bfs

        stack = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    stack.append((i,j))
        

        while stack:
            i,j = stack.pop(0)
            for direc in [(0,1), (1,0), (0,-1), (-1,0)]:
                newi, newj = i + direc[0], j + direc[1]
                if (0 <= newi < len(grid) 
                    and 0 <= newj < len(grid[0]) 
                    and grid[newi][newj] ==  2147483647):
                    grid[newi][newj] = grid[i][j] + 1
                    stack.append((newi,newj))
        

