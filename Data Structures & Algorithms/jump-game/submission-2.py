class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tar = len(nums) -1
        cur = len(nums) - 1
        while cur >= 0:
            if (tar-cur) <= nums[cur]:
                tar = cur
            cur -= 1
        return tar == 0