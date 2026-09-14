class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0

        def dfs(i,j):
            grid[i][j] = "-1"
            
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]

            for x,y in dirs:
                if 0 <= (i + x) < len(grid) and 0 <= (j + y) < len(grid[0]) and grid[i+x][j+y] == "1":
                    dfs(i+x, j+y)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    out += 1
                    dfs(i,j)
        return out