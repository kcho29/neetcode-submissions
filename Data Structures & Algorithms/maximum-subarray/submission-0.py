class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        cur = 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maximum = max(maximum, cur)
        return maximum