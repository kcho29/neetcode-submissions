class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def solve(n):
            if n >= len(nums):
                return 0
            
            if memo[n] != -1:
                return memo[n]
            
            memo[n] = max(solve(n+1), nums[n] + solve(n+2))
            return memo[n]

        return max(solve(0), solve(1))