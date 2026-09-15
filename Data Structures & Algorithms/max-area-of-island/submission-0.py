class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        if not grid:
             return 0
        
        def dfs(i,j):
            out = 0
            grid[i][j] = -1

            for idir, jdir in [(1,0), (0,1), (-1,0), (0,-1)]:
                newi, newj = i + idir, j + jdir
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and grid[newi][newj] == 1:
                    out += dfs(newi, newj)
            return out + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i,j))

        return maxarea