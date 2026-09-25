class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        out = [-1] * len(cost)

        def dfs(n):
            if n >= len(cost):
                return 0
            if out[n] != -1:
                return out[n]
            
            out[n] = cost[n] + min(dfs(n+1), dfs(n+2))
            return out[n]
        return min(dfs(0), dfs(1))