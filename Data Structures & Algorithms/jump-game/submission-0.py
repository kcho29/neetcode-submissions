class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        while cur < len(nums)-1:
            if nums[cur] == 0:
                return False
            cur += nums[cur]
        return cur == len(nums)-1