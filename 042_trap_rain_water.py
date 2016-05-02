# 52nd percentile on speed.

class Solution(object):
    def trap(self, height):
        
        max_height = -1
        left_max = []
        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
            left_max.append(max_height)
        
        max_height = -1
        right_max = []
        for i in range(len(height) - 1, -1, -1):
            if height[i] > max_height:
                max_height = height[i]
            right_max.append(max_height)
        right_max.reverse()
        
        total_water = 0
        for i in range(len(height)):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                total_water += water 
        
        return total_water