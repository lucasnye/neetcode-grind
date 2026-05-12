class Solution:
    def maxArea(self, heights: List[int]) -> int:
        capacity = volume = 0
        n = len(heights)
        p1, p2 = 0, n - 1
        while p1 < p2:
            if heights[p1] > heights[p2]:
                height = heights[p2]
                volume = height * (p2 - p1)
                p2 -= 1
            elif heights[p1] < heights[p2]:
                height = heights[p1]
                volume = height * (p2 - p1)
                p1 += 1
            else:
                height = heights[p1]
                volume = height * (p2 - p1)
                p1 += 1
            
            if capacity < volume:
                capacity = volume
            
        return capacity