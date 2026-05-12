class Solution:
    def trap(self, height: List[int]) -> int:
        # water = 0
        # p1 = 0
        # p2 = p1 + 1
        # n = len(height)
        # if n < 3:
        #     return water
        # # Move to first possible left wall of container
        # while height[p1] == 0 or height[p1] < height[p2]:
        #     p1 += 1
        #     p2 += 1
        #     if p2 > n - 1:
        #         break
        # # 
        # while p2 + 1 < n - 1:
        #     while height[p2 + 1] < height[p2]:
        #         p2 += 1
        #         if p2 + 1 > n - 1:
        #             break
        #     # lowest = height[p2]
        #     while p2 + 1 < n and height[p2 + 1] > height[p2]:
        #         p2 += 1
        #         if p2 + 1 > n - 1:
        #             break
        #     if height[p2] < height[p1]:
        #         for i in range(p2, n):
        #             if height[i] > height[p2]:
        #                 p2 = i
        #     w = p2 - p1 - 1
        #     h = min(height[p1], height[p2])
        #     rect = w * h
        #     p1 += 1
        #     while p1 < p2:
        #         rect -= height[p1]
        #         p1 += 1
        #     water += rect
        #     if p2 + 1 < n - 1:
        #         p2 += 1
        

        # while p2 + 1 < n - 1:
        #     # Find right wall of container
        #     while height[p2 + 1] < height[p1]:
        #         p2 += 1
        #         if p2 + 1 > n - 1:
        #             return water
        #     width = p2 - p1
        #     # if p2 + 1 > n - 1:
        #     #     break
        #     p2 += 1
        #     h = min(height[p1], height[p2])
        #     rectangle = width * h
        #     p1 += 1
        #     while p1 < p2:
        #         rectangle -= height[p1]
        #         p1 += 1
        #     water += rectangle
        #     p2 += 1

        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        
        return water