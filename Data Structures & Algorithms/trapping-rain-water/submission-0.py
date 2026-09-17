class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        out = 0
        lmax, rmax = height[left], height[right]

        while left < right:
            if lmax > rmax:
                right -= 1
                rmax = max(rmax, height[right])
                out += rmax-height[right]
            else:
                left += 1
                lmax = max(lmax, height[left])
                out += lmax-height[left]

        return out