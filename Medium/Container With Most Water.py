# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        
        size = len(height)
        
        max_width = size - 1
        
        l = 0
        r = size - 1
        
        for width in range(max_width, 0, -1):
            
            if height[l] < height[r]:
                area = max(area, width*height[l])
                l += 1
            else:
                area = max(area, width*height[r])
                r -= 1
                
        return area
