class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Looking for insetion points for target +/- 0.5
        # Approach: Do binary search twice
        if not nums:
            return [-1,-1]
        low1 = 0 
        high1 = len(nums)
        while low1 < high1:
            mid = (low1 + high1) // 2
            if nums[mid] < target - 0.5:
                low1 = mid + 1
            else:
                high1 = mid
        if low1 == len(nums) or nums[low1] != target:
            return [-1,-1]
        low2 = 0 
        high2 = len(nums)
        while low2 < high2:
            mid = (low2 + high2) // 2
            if nums[mid] <= target + 0.5:
                low2 = mid + 1
            else:
                high2 = mid

        return [low1, low2-1]