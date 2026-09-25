class Solution:
    def climbStairs(self, n: int) -> int:
        memor = {}

        def solve(n):
            if n <= 2:
                return n
            if n in memor:
                return memor[n]
            
            memor[n] = solve(n-1) + solve(n-2)
            return memor[n]
        
        return solve(n)