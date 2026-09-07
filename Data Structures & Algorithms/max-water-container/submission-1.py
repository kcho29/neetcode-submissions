class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        area = 0
        while start < end:
            area = max(area, min(heights[start], heights[end])*(end-start))
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return area