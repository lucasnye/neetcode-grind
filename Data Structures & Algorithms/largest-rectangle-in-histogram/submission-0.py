class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = None
        for i, height in enumerate(heights):
            if not max_rect:
                max_rect = height
                continue
            j = i
            local_min = height
            while j >= 0:
                local_min = min(local_min, heights[j])
                prev = local_min * (i - j + 1)
                max_rect = max(prev, max_rect)
                j -= 1
        return max_rect